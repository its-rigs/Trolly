import json
import httplib2

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

import trolly


class Client(object):

    '''
    A class that has all the logic for communicating with Trello and returning
    information to the user
    '''

    def __init__(self, api_key, user_auth_token=None):
        '''
        Takes the API key and User Auth Token, which are needed for all Trello
        API calls to allow access to requested information
        '''
        self.api_key = api_key
        self.user_auth_token = user_auth_token

        self.client = httplib2.Http()

    def add_authorisation(self, query_params):
        '''
        Adds the API key and user auth token to the query parameters
        '''
        query_params['key'] = self.api_key

        if self.user_auth_token:
            query_params['token'] = self.user_auth_token

        return query_params

    def clean_path(self, path):
        '''
        Ensure the path has a preceding /
        '''
        if path[0] != '/':
            path = '/' + path
        return path

    def check_errors(self, uri, response):
        '''
        Check HTTP reponse for known errors
        '''
        if response.status == 401:
            raise trolly.Unauthorised(uri, response)

        if response.status != 200:
            raise trolly.ResourceUnavailable(uri, response)

    def build_uri(self, path, query_params):
        '''
        Build the URI for the API call.
        '''
        url = 'https://api.trello.com/1' + self.clean_path(path)
        url += '?' + urlencode(query_params)

        return url

    def fetch_json(self, uri_path, http_method='GET', query_params=None,
                   body=None, headers=None):
        '''
        Make a call to Trello API and capture JSON response. Raises an error
        when it fails.

        Returns:
            dict: Dictionary with the JSON data
        '''
        query_params = query_params or {}
        headers = headers or {}

        query_params = self.add_authorisation(query_params)
        uri = self.build_uri(uri_path, query_params)

        allowed_methods = ("POST", "PUT", "DELETE")
        if http_method in allowed_methods and 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        headers['Accept'] = 'application/json'
        response, content = self.client.request(
            uri=uri,
            method=http_method,
            body=body,
            headers=headers
        )

        self.check_errors(uri, response)

        return json.loads(content.decode('utf-8'))

    def create_organisation(self, organisation_json):
        '''
        Create an Organisation object from a JSON object

        Returns:
            Organisation: The organisation from the given `organisation_json`.
        '''
        return trolly.organisation.Organisation(
            trello_client=self,
            organisation_id=organisation_json['id'],
            name=organisation_json['name'],
            data=organisation_json,
        )

    def create_board(self, board_json):
        '''
        Create Board object from a JSON object

        Returns:
            Board: The board from the given `board_json`.
        '''
        return trolly.board.Board(
            trello_client=self,
            board_id=board_json['id'],
            name=board_json['name'],
            data=board_json,
        )

    def create_label(self, label_json):
        '''
        Create Label object from JSON object

        Returns:
            Label: The label from the given `label_json`.
        '''
        return trolly.label.Label(
            trello_client=self,
            label_id=label_json['id'],
            name=label_json['name'],
            data=label_json,
        )

    def create_list(self, list_json):
        '''
        Create List object from JSON object

        Returns:
            List: The list from the given `list_json`.
        '''
        return trolly.list.List(
            trello_client=self,
            list_id=list_json['id'],
            name=list_json['name'],
            data=list_json,
        )

    def create_card(self, card_json):
        '''
        Create a Card object from JSON object

        Returns:
            Card: The card from the given `card_json`.
        '''
        return trolly.card.Card(
            trello_client=self,
            card_id=card_json['id'],
            name=card_json['name'],
            data=card_json,
        )

    def create_checklist(self, checklist_json):
        '''
        Create a Checklist object from JSON object

        Returns:
            Checklist: The checklist from the given `checklist_json`.
        '''
        return trolly.checklist.Checklist(
            trello_client=self,
            checklist_id=checklist_json['id'],
            name=checklist_json['name'],
            data=checklist_json,
        )

    def create_member(self, member_json):
        '''
        Create a Member object from JSON object

        Returns:
            Member: The member from the given `member_json`.
        '''
        return trolly.member.Member(
            trello_client=self,
            member_id=member_json['id'],
            name=member_json['fullName'],
            data=member_json,
        )

    def get_organisation(self, id, name=None):
        '''
        Get an organisation

        Returns:
            Organisation: The organisation with the given `id`
        '''
        return self.create_organisation(dict(id=id, name=name))

    def get_board(self, id, name=None):
        '''
        Get a board

        Returns:
            Board: The board with the given `id`
        '''
        return self.create_board(dict(id=id, name=name))

    def get_list(self, id, name=None):
        '''
        Get a list

        Returns:
            List: The list with the given `id`
        '''
        return self.create_list(dict(id=id, name=name))

    def get_card(self, id, name=None):
        '''
        Get a card

        Returns:
            Card: The card with the given `id`
        '''
        return self.create_card(dict(id=id, name=name))

    def get_checklist(self, id, name=None):
        '''
        Get a checklist

        Returns:
            Checklist: The checklist with the given `id`
        '''
        return self.create_checklist(dict(id=id, name=name))

    def get_member(self, id='me', name=None):
        '''
        Get a member or your current member if `id` wasn't given.

        Returns:
            Member: The member with the given `id`, defaults to the
            logged in member.
        '''
        return self.create_member(dict(id=id, fullName=name))

    # Shortcut methods from the current member
    def get_boards(self, **query_params):
        '''
        Get all boards this member is attached to. Returns a list of Board
        objects.

        Returns:
            list(Board): Return all boards for this member
        '''
        return self.get_member().get_boards(**query_params)

    def get_cards(self, **query_params):
        '''
        Get all cards this member is attached to. Return a list of Card
        objects.

        Returns:
            list(Card): Return all cards this member is attached to
        '''
        return self.get_member().get_cards(**query_params)

    def get_organisations(self, **query_params):
        '''
        Get all organisations this member is part of. Return a list of
        Organisation objects.

        Returns:
            list(Organisation): Return all organisations this member is
            part of
        '''
        return self.get_member().get_organisations(**query_params)


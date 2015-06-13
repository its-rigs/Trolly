"""
Created on 8 Nov 2012

@author: plish
"""

import json
from httplib2 import Http

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from trolly.organisation import Organisation
from trolly.board import Board
from trolly.list import List
from trolly.card import Card
from trolly.checklist import Checklist
from trolly.member import Member

from trolly import Unauthorised, ResourceUnavailable


class Client(object):
    """
    A class that has all the logic for communicating with Trello and returning
    information to the user
    """

    def __init__(self, api_key, user_auth_token=None):
        """
        Takes the API key and User Auth Token, which are needed for all Trello
        API calls to allow access to requested information
        """
        self.api_key = api_key
        self.user_auth_token = user_auth_token

        self.client = Http()

    def add_authorisation(self, query_params):
        """
        Adds the API key and user auth token to the query parameters
        """
        query_params['key'] = self.api_key

        if self.user_auth_token:
            query_params['token'] = self.user_auth_token

        return query_params

    def clean_path(self, path):
        """
        Ensure the path has a preceding /
        """
        if path[0] != '/':
            path = '/' + path
        return path

    def check_errors(self, uri, response):
        """
        Check HTTP reponse for known errors
        """
        if response.status == 401:
            raise Unauthorised(uri, response)

        if response.status != 200:
            raise ResourceUnavailable(uri, response)

    def build_uri(self, path, query_params):
        """
        Build the URI for the API call.
        """
        url = 'https://api.trello.com/1' + self.cleanPath(path)
        url += '?' + urlencode(query_params)

        return url

    def fetch_json(self, uri_path, http_method='GET', query_params=None, body=None, headers=None):
        """
        Make a call to Trello API and capture JSON response. Raises an error
        when it fails.
        """
        query_params = query_params or {}
        headers = headers or {}

        query_params = self.add_authorisation(query_params)
        uri = self.build_uri(uri_path, query_params)

        if http_method in ("POST", "PUT", "DELETE") and 'Content-Type' not in headers:
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
        """
        Create an Organisation object from a JSON object
        """
        return Organisation(
            trello_client=self,
            organisation_id=organisation_json['id'],
            name=organisation_json['name']
        )

    def create_board(self, board_json):
        """
        Create Board object from a JSON object
        """
        return Board(
            trello_client=self,
            board_id=board_json['id'],
            name=board_json['name']
        )

    def create_list(self, list_json):
        """
        Create List object from JSON object
        """
        return List(
            trello_client=self,
            list_id=list_json['id'],
            name=list_json['name']
        )

    def create_card(self, card_json):
        """
        Create a Card object from JSON object
        """
        return Card(
            trello_client=self,
            card_id=card_json['id'],
            name=card_json['name']
        )

    def create_checklist(self, checklist_json):
        """
        Create a Checklist object from JSON object
        """
        return Checklist(
            trello_client=self,
            checklist_id=checklist_json['id'],
            name=checklist_json['name']
        )

    def create_member(self, member_json):
        """
        Create a Member object from JSON object
        """
        return Member(
            trello_client=self,
            member_id=member_json['id'],
            name=member_json['fullName']
        )

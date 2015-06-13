from trolly.trelloobject import TrelloObject


class Board(TrelloObject):

    """
    Class representing a Trello Board
    """

    def __init__(self, trello_client, board_id, name=''):
        super(Board, self).__init__(trello_client)

        self.id = board_id
        self.name = name

        self.base_uri = '/boards/' + self.id

    def get_board_information(self, query_params=None):
        """
        Get all information for this board. Returns a dictionary of values.
        """
        return self.fetch_json(
            uri_path='/boards/' + self.id,
            query_params=query_params or {}
        )

    def get_lists(self):
        """
        Get the lists attached to this board. Returns a list of List objects.
        """
        lists = self.get_lists_json(self.base_uri)

        lists_list = []
        for list_json in lists:
            lists_list.append(self.create_list(list_json))

        return lists_list

    def get_cards(self):
        """
        Get the cards for this board. Returns a list of Card objects.
        """
        cards = self.get_cards_json(self.base_uri)

        cards_list = []
        for card_json in cards:
            cards_list.append(self.create_card(card_json))

        return cards_list

    def get_card(self, card_id):
        """
        Get a Card for a given card id. Returns a Card object.
        """
        card_json = self.fetch_json(
            uri_path=self.base_uri + '/cards/' + card_id
        )

        return self.create_card(card_json)

    def get_members(self):
        """
        Get Members attached to this board. Returns a list of Member objects.
        """
        members = self.get_members_json(self.base_uri)

        members_list = []
        for member_json in members:
            members_list.append(self.create_member(member_json))

        return members_list

    def get_organisation(self):
        """
        Get the Organisation for this board. Returns Organisation object.
        """
        organisation_json = self.get_organisations_json(self.base_uri)

        return self.create_organisation(organisation_json)

    def update_board(self, query_params=None):
        """
        Update this board's information. Returns a new board.
        """
        board_json = self.fetch_json(
            uri_path=self.base_uri,
            http_method='PUT',
            query_params=query_params or {}
        )

        return self.create_board(board_json)

    def add_list(self, query_params=None):
        """
        Create a list for a board. Returns a new List object.
        """
        list_json = self.fetch_json(
            uri_path=self.base_uri + '/lists',
            http_method='POST',
            query_params=query_params or {}
        )

        return self.create_list(list_json)

    def add_member_by_id(self, member_id, membership_type='normal'):
        """
        Add a member to the board using the id. Membership type can be
        normal or admin. Returns JSON of all members if successful or raises an
        Unauthorised exception if not.
        """
        return self.fetch_json(
            uri_path=self.base_uri + '/members/%s' % member_id,
            http_method='PUT',
            query_params={
                'type': membership_type
            }
        )

    def add_member(self, email, fullname, membership_type='normal'):
        """
        Add a member to the board. Membership type can be normal or admin.
        Returns JSON of all members if successful or raises an Unauthorised
        exception if not.
        """
        return self.fetch_json(
            uri_path=self.base_uri + '/members',
            http_method='PUT',
            query_params={
                'email': email,
                'fullName': fullname,
                'type': membership_type
            }
        )

    def remove_member(self, member_id):
        """
        Remove a member from the organisation.Returns JSON of all members if
        successful or raises an Unauthorised exception if not.
        """
        return self.fetch_json(
            uri_path=self.base_uri + '/members/%s' % member_id,
            http_method='DELETE'
        )

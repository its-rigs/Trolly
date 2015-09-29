from . import trelloobject


class Member(trelloobject.TrelloObject):

    '''
    Class representing a Trello Member
    '''

    def __init__(self, trello_client, member_id, name='', **kwargs):
        super(Member, self).__init__(trello_client, **kwargs)
        self.id = member_id
        self.name = name

        self.base_uri = '/members/' + self.id

    def get_member_information(self, query_params=None):
        '''
        Get Information for a member. Returns a dictionary of values.

        Returns:
            dict
        '''
        return self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

    def get_boards(self):
        '''
        Get all boards this member is attached to. Returns a list of Board
        objects.

        Returns:
            list(Board): Return all boards for this member
        '''
        boards = self.get_boards_json(self.base_uri)

        boards_list = []
        for board_json in boards:
            boards_list.append(self.create_board(board_json))

        return boards_list

    def get_cards(self):
        '''
        Get all cards this member is attached to. Return a list of Card
        objects.

        Returns:
            list(Card): Return all cards this member is attached to
        '''
        cards = self.get_cards_json(self.base_uri)

        cards_list = []
        for card_json in cards:
            cards_list.append(self.create_card(card_json))

        return cards_list

    def get_organisations(self):
        '''
        Get all organisations this member is attached to. Return a list of
        Organisation objects.

        Returns:
            list(Organisation): Return all organisations this member is
            attached to
        '''
        organisations = self.get_organisations_json(self.base_uri)

        organisations_list = []
        for organisation_json in organisations:
            organisations_list.append(
                self.create_organisation(organisation_json))

        return organisations_list

    def create_new_board(self, query_params=None):
        '''
        Create a new board. name is required in query_params. Returns a Board
        object.

        Returns:
            Board: Returns the created board
        '''
        board_json = self.fetch_json(
            uri_path='/boards',
            http_method='POST',
            query_params=query_params or {}
        )
        return self.create_board(board_json)

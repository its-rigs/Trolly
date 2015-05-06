"""
Created on 9 Nov 2012

@author: plish
"""

from trolly.trelloobject import TrelloObject


class Member(TrelloObject):
    """
    Class representing a Trello Member
    """

    def __init__(self, trello_client, member_id, name=''):

        super(Member, self).__init__(trello_client)
        self.id = member_id
        self.name = name

        self.base_uri = '/members/' + self.id

    def get_member_information(self, query_params=None):
        """
        Get Information for a member. Returns a dictionary of values.
        """
        return self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

    def get_boards(self):
        """
        Get all boards this member is attached to. Returns a list of Board objects.
        """
        boards = self.get_boards_json(self.base_uri)

        boards_list = []
        for board_json in boards:
            boards_list.append(self.create_board(board_json))

        return boards_list

    def get_cards(self):
        """
        Get all cards this member is attached to. Return a list of Card objects.
        """
        cards = self.get_cards_json(self.base_uri)

        cards_list = []
        for card_json in cards:
            cards_list.append(self.create_card(card_json))

        return cards_list

    def create_new_board(self, query_params=None):
        """
        Create a new board. name is required in query_params. Returns a Board object.
        """
        board_json = self.fetch_json(
            uri_path='/boards',
            http_method='POST',
            query_params=query_params or {}
        )
        return self.create_board(board_json)

    # Deprecated
    def getMemberInformation(self, query_params=None):
        return self.get_member_information(query_params)

    def getBoards(self):
        return self.get_boards()

    def getCards(self):
        return self.get_cards()

    def createNewBoard(self, query_params=None):
        return self.create_new_board(query_params)

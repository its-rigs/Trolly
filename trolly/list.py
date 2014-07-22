"""
Created on 8 Nov 2012

@author: plish
"""

from trolly.trelloobject import TrelloObject


class List(TrelloObject):
    """
    Class representing a Trello List
    """

    def __init__(self, trello_client, list_id, name=''):
        super(List, self).__init__(trello_client)

        self.id = list_id
        self.name = name

        self.base_uri = '/lists/' + self.id

    def getListInformation(self, query_params={}):
        """
        Get information for this list. Returns a dictionary of values.
        """
        return self.fetchJson(
            uri_path=self.base_uri,
            query_params=query_params
        )

    def getBoard(self):
        """
        Get the board that this list belongs to. Returns a Board object.
        """
        board_json = self.getBoardJson(self.base_uri)

        return self.createBoard(board_json)

    def getCards(self):
        """
        Get cards for this list. Returns a list of Card objects
        """
        cards = self.getCardsJson(self.base_uri)

        cards_list = []
        for card_json in cards:
            cards_list.append(self.createCard(card_json))

        return cards_list

    def updateList(self, query_params={}):
        """
        Update information for this list. Returns a new List object.
        """
        list_json = self.fetchJson(
            uri_path=self.base_uri,
            http_method='PUT',
            query_params=query_params
        )

        return self.createList(list_json)

    def addCard(self, query_params={}):
        """
        Create a card for this list. Returns a Card object.
        """
        card_json = self.fetchJson(
            uri_path=self.base_uri + '/cards',
            http_method='POST',
            query_params=query_params
        )

        return self.createCard(card_json)

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

    def get_list_information(self, query_params=None):
        """
        Get information for this list. Returns a dictionary of values.
        """
        return self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

    def get_board(self):
        """
        Get the board that this list belongs to. Returns a Board object.
        """
        board_json = self.get_board_json(self.base_uri)
        return self.create_board(board_json)

    def get_cards(self):
        """
        Get cards for this list. Returns a list of Card objects
        """
        cards = self.get_cards_json(self.base_uri)

        cards_list = []
        for card_json in cards:
            cards_list.append(self.create_card(card_json))

        return cards_list

    def update_list(self, query_params=None):
        """
        Update information for this list. Returns a new List object.
        """
        list_json = self.fetch_json(
            uri_path=self.base_uri,
            http_method='PUT',
            query_params=query_params or {}
        )

        return self.create_list(list_json)

    def add_card(self, query_params=None):
        """
        Create a card for this list. Returns a Card object.
        """
        card_json = self.fetch_json(
            uri_path=self.base_uri + '/cards',
            http_method='POST',
            query_params=query_params or {}
        )

        return self.create_card(card_json)

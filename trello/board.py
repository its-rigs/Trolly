'''
Created on 8 Nov 2012

@author: plish
'''

from trelloobject import TrelloObject


class Board( TrelloObject ):
    """
    Class representing a Trello Board
    """

    def __init__( self, trello_client, board_id, name = '' ):

        super( Board, self ).__init__( trello_client )

        self.id = board_id
        self.name = name

        self.base_uri = '/boards/' + self.id


    def getBoardInformation( self, query_params = {} ):
        """
        Get all information for this board. Returns a dictionary of values.
        """
        return self.fetchJson( 
                uri_path = '/boards/' + self.id,
                query_params = query_params
            )


    def getLists( self ):
        """
        Get the lists attached to this board. Returns a list of List objects.
        """
        lists = self.getListsJson( self.base_uri )

        lists_list = []
        for list_json in lists:
            lists_list.append( self.createList( list_json ) )

        return lists_list


    def getCards( self ):
        """
        Get the cards for this board. Returns a list of Card objects.
        """
        cards = self.getCardsJson( self.base_uri )

        cards_list = []
        for card_json in cards:
            cards_list.append( self.createCard( card_json ) )

        return cards_list


    def getCard( self, card_id ):
        """
        Get a Card for a given card id. Returns a Card object.
        """
        card_json = self.fetchJson( 
                uri_path = self.base_uri + '/cards/' + card_id
            )

        return self.createCard( card_json )


    def getMembers( self ):
        """
        Get Members attached to this board. Returns a list of Member objects.
        """
        members = self.getMembersJson( self.base_uri )

        members_list = []
        for member_json in members:
            members_list.append( self.createMember( member_json ) )

        return members_list


    def getOrganisation( self ):
        """
        Get the Organisation for this board. Returns Organisation object.
        """
        organisation_json = self.getOrganisationsJson( self.base_uri )

        return self.createOrganisation( organisation_json )


    def updateBoard( self, query_params = {} ):
        """
        Update this board's information. Returns a new board.
        """
        board_json = self.fetchJson( 
                uri_path = self.base_uri,
                http_method = 'PUT',
                query_params = query_params
            )

        return self.createBoard( board_json )


    def addList( self, query_params = {} ):
        """
        Create a list for a board. Returns a new List object.
        """
        list_json = self.fetchJson( 
                uri_path = self.base_uri + '/lists',
                http_method = 'POST',
                query_params = query_params
            )

        return self.createList( list_json )













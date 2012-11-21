'''
Created on 9 Nov 2012

@author: plish
'''

from trelloobject import TrelloObject


class Member( TrelloObject ):
    """
    Class representing a Trello Member
    """

    def __init__( self, trello_client, member_id, name = '' ):

        super( Member, self ).__init__( trello_client )
        self.id = member_id
        self.name = name

        self.base_uri = '/members/' + self.id


    def getMemberInformation( self, query_params = {} ):
        """
        Get Information for a memeber. Returns a dictionary of values.
        """
        return self.fetchJson( 
                uri_path = self.base_uri,
                query_params = query_params
            )


    def getBoards( self ):
        """
        Get all boards this member is attached to. Returns a list of Board objects.
        """
        boards = self.getBoardsJson( self.base_uri )

        boards_list = []
        for board_json in boards:
            boards_list.append( self.createBoard( board_json ) )

        return boards_list


    def getCards( self ):
        """
        Get all cards this member is attached to. Return a list of Card objects.
        """
        cards = self.getCardsJson( self.base_uri )

        cards_list = []
        for card_json in cards:
            cards_list.append( self.createCard( card_json ) )

        return cards_list

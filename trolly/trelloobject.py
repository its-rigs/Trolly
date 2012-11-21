'''
Created on 9 Nov 2012

@author: plish
'''

class TrelloObject( object ):
    """
    This class is a base object that should be used by all trello objects;
    Board, List, Card, etc. It contains methods needed and used by all those
    objects and masks the client calls as methods belonging to the object.
    """

    def __init__( self, trello_client ):
        """
        A Trello client, Oauth of HTTP client is required for each object.
        """
        super( TrelloObject, self ).__init__()

        self.client = trello_client


    def fetchJson( self, uri_path, http_method = 'GET', query_params = {}, body = None, headers = {} ):

        return self.client.fetchJson( 
                uri_path = uri_path,
                http_method = http_method,
                query_params = query_params,
                body = body,
                headers = headers,
            )


    def getOrganisationsJson( self, base_uri ):
        return self.fetchJson( base_uri + '/organization' )


    def getBoardsJson( self, base_uri ):
        return self.fetchJson( base_uri + '/boards' )


    def getBoardJson( self, base_uri ):
        return self.fetchJson( base_uri + '/board' )


    def getListsJson( self, base_uri ):
        return self.fetchJson( base_uri + '/lists' )


    def getListJson( self, base_uri ):
        return self.fetchJson( base_uri + '/list' )


    def getCardsJson( self, base_uri ):
        return self.fetchJson( base_uri + '/cards' )


    def getChecklistsJson( self, base_uri ):
        return self.fetchJson( base_uri + '/checklists' )


    def getMembersJson( self, base_uri ):
        return self.fetchJson( base_uri + '/members' )


    def createOrganisation( self, oranisation_json, **kwargs ):
        return self.client.createOrganisation( oranisation_json, **kwargs )


    def createBoard( self, board_json, **kwargs ):
        return self.client.createBoard( board_json, **kwargs )


    def createList( self, list_json, **kwargs ):
        return self.client.createList( list_json, **kwargs )


    def createCard( self, card_json, **kwargs ):
        return self.client.createCard( card_json, **kwargs )


    def createChecklist( self, checklist_json, **kwargs ):
        return self.client.createChecklist( checklist_json, **kwargs )


    def createMember( self, member_json, **kwargs ):
        return self.client.createMember( member_json, **kwargs )

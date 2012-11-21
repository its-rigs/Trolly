'''
Created on 8 Nov 2012

@author: plish
'''

import mimetypes

from trelloobject import TrelloObject


class Card( TrelloObject ):
    """
    Class representing a Trello Card
    """

    def __init__( self, trello_client, card_id, name = '' ):

        super( Card, self ).__init__( trello_client )

        self.id = card_id
        self.name = name

        self.base_uri = '/cards/' + self.id


    def getCardInformation( self, query_params = {} ):
        """
        Get information for this card. Returns a dictionary of values.
        """
        return self.fetchJson( 
                uri_path = self.base_uri,
                query_params = query_params
            )


    def getBoard( self ):
        """
        Get board information for this card. Returns a Board object.
        """
        board_json = self.getBoardJson( self.base_uri )
        return self.createBoard( board_json )


    def getList( self ):
        """
        Get list information for this card. Returns a List object.
        """
        list_json = self.getListJson( self.base_uri )

        return self.createList( list_json )


    def getChecklists( self ):
        """
        Get the checklists for this card. Returns a list of Checklist objects.
        """
        checklists = self.getChecklistsJson( self.base_uri )

        checklists_list = []
        for checklist_json in checklists:
            checklists_list.append( self.createChecklist( checklist_json ) )

        return checklists_list


    def getMembers( self ):
        """
        Get all members attached to this card. Returns a list of Member objects.
        """
        members = self.getMembersJson( self.base_uri )

        members_list = []
        for member_json  in members:
            members_list.append( self.createMember( member_json ) )

        return members_list


    def updateCard( self, query_params = {} ):
        """
        Update information for this card. Returns a new Card object.
        """
        card_json = self.fetchJson( 
                uri_path = self.base_uri,
                http_method = 'PUT',
                query_params = query_params
            )

        return self.createCard( card_json )


    def addComments( self, comment_text ):
        """
        Adds a comment to this card by the current user.
        """
        return self.fetchJson( 
                uri_path = self.base_uri + '/actions/comments',
                http_method = 'POST',
                query_params = { 'text': comment_text }
            )


    def addAttachment( self, filename, open_file ):
        """
        Adds an attachement to this card.
        """
        fields = {
                'api_key': self.client.api_key,
                'token': self.client.user_auth_token
            }

        content_type, body = self.encodeMultipartFormdata( 
                fields = fields,
                filename = filename,
                file_values = open_file
            )

        return self.fetchJson( 
                uri_path = self.base_uri + '/attachments',
                http_method = 'POST',
                body = body,
                headers = { 'Content-Type': content_type },
            )



    def addChecklists( self, query_params = {} ):
        """
        Add a checklist to this card. Returns a Checklist object.
        """
        checklist_json = self.fetchJson( 
                uri_path = self.base_uri + '/checklists',
                http_method = 'POST',
                query_params = query_params
            )

        return self.createChecklist( checklist_json )


    def addLabels( self, query_params = {} ):
        """
        Add a label to this card.
        """
        return self.fetchJson( 
                uri_path = self.base_uri + '/labels',
                http_method = 'POST',
                query_params = query_params
            )


    def addMember( self, member_id ):
        """
        Add a member to this card. Returns a list of Member objects.
        """
        members = self.fetchJson( 
                uri_path = self.base_uri + '/members',
                http_method = 'POST',
                query_params = { 'value': member_id }
            )

        members_list = []
        for member_json in members:
            members_list.append( self.createMember( member_json ) )

        return members_list


    def removeMember( self, member_id ):
        """
        Remove a member from this card.
        """
        return self.fetchJson( 
                uri_path = self.base_uri + '/members/' + member_id,
                http_method = 'DELETE'
            )


    def encodeMultipartFormdata( self, fields, filename, file_values ):
        """
        Encodes data to updload a file to Trello.
        Fields is a dictionary of api_key and token. Filename is the name of the
        file and file_values is the open(file).read() string.
        """
        boundary = '----------Trello_Boundary_$'
        crlf = '\r\n'

        data = []

        for key in fields:
            data.append( '--' + boundary )
            data.append( 'Content-Disposition: form-data; name="%s"' % key )
            data.append( '' )
            data.append( fields[key] )

        data.append( '--' + boundary )
        data.append( 'Content-Disposition: form-data; name="file"; filename="%s"' % ( filename ) )
        data.append( 'Content-Type: %s' % self.getContentType( filename ) )
        data.append( '' )
        data.append( file_values )

        data.append( '--' + boundary + '--' )
        data.append( '' )

        body = crlf.join( data )
        content_type = 'multipart/form-data; boundary=%s' % boundary

        return content_type, body


    def getContentType( self, filename ):
        return mimetypes.guess_type( filename )[0] or 'application/octet-stream'






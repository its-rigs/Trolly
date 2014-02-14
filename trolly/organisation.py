'''
Created on 14 Nov 2012

@author: plish
'''

from trolly.trelloobject import TrelloObject


class Organisation( TrelloObject ):

    def __init__( self, trello_client, organisation_id, name = '' ):
        super( Organisation, self ).__init__( trello_client )

        self.id = organisation_id
        self.name = name

        self.base_uri = '/organizations/' + self.id


    def getOrganisationInformation( self, query_params = {} ):
        """
        Get information fot this organisation. Returns a dictionary of values.
        """
        return self.fetchJson(
                uri_path = self.base_uri,
                query_params = query_params
            )


    def getBoards( self ):
        """
        Get all the boards for this organisation. Returns a list of Board s.
        """
        boards = self.getBoardsJson( self.base_uri )

        boards_list = []
        for board_json in boards:
            boards_list.append( self.createBoard( board_json ) )

        return boards_list


    def getMembers( self ):
        """
        Get all members attached to this organisation. Returns a list of
        Member objects
        """
        members = self.getMembersJson( self.base_uri )

        members_list = []
        for member_json in members:
            members_list.append( self.createMember( member_json ) )

        return members_list


    def updateOrganisation( self, query_params = {} ):
        """
        Update this organisations information. Returns a new organisation object.
        """
        organisation_json = self.fetchJson(
                uri_path = self.base_uri,
                http_method = 'PUT',
                query_params = query_params
            )

        return self.createOrganisation( organisation_json )


    def removeMember( self, member_id ):
        """
        Remove a member from the organisation.Returns JSON of all members if
        successful or raises an Unauthorised exception if not.
        """
        return self.fetchJson(
                uri_path = self.base_uri + '/members/%s' % ( member_id ),
                http_method = 'DELETE'
            )


    def addMemberById( self, member_id, membership_type = 'normal' ):
        """
        Add a member to the board using the id. Membership type can be
        normal or admin. Returns JSON of all members if successful or raises an
        Unauthorised exception if not.
        """
        return self.fetchJson(
                uri_path = self.base_uri + '/members/%s' % ( member_id ),
                http_method = 'PUT',
                query_params = {
                    'type': membership_type
                }
            )


    def addMember( self, email, fullname, membership_type = 'normal' ):
        """
        Add a member to the board. Membership type can be normal or admin.
        Returns JSON of all members if successful or raises an Unauthorised
        exception if not.
        """
        return self.fetchJson(
                uri_path = self.base_uri + '/members',
                http_method = 'PUT',
                query_params = {
                    'email': email,
                    'fullName': fullname,
                    'type': membership_type
                }
            )

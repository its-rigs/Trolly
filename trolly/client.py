'''
Created on 8 Nov 2012

@author: plish
'''

import json
from httplib2 import Http
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from trolly.organisation import Organisation
from trolly.board import Board
from trolly.list import List
from trolly.card import Card
from trolly.checklist import Checklist
from trolly.member import Member

from trolly import Unauthorised, ResourceUnavailable


class Client( object ):
    """
    A class that has all the logic for communicating with Trello and returning
    information to the user
    """

    def __init__( self, api_key, user_auth_token = None ):
        """
        Takes the API key and User Auth Token, which are needed for all Trello
        API calls to allow access to requested information
        """
        self.api_key = api_key
        self.user_auth_token = user_auth_token

        self.client = Http()


    def addAuthorisation( self, query_params ):
        """
        Adds the API key and user auth token to the query parameters
        """
        query_params['key'] = self.api_key

        if self.user_auth_token:
            query_params['token'] = self.user_auth_token

        return query_params


    def cleanPath( self, path ):
        """
        Ensure the path has a preceeding /
        """
        if path[0] != '/':
            path = '/' + path
        return path


    def checkErrors( self, uri, response ):
        """
        Check HTTP reponse for known errors
        """
        if response.status == 401:
            raise Unauthorised( uri, response )

        if response.status != 200:
            raise ResourceUnavailable( uri, response )


    def buildUri( self, path, query_params ):
        """
        Build the URI for the API call.
        """
        url = 'https://api.trello.com/1' + self.cleanPath( path )
        url += '?' + urlencode( query_params )

        return url


    def fetchJson( self, uri_path, http_method = 'GET', query_params = {}, body = None, headers = {} ):
        """
        Make a call to Trello API and capture JSON response. Raises an error
        when it fails.
        """
        query_params = self.addAuthorisation( query_params )
        uri = self.buildUri( uri_path, query_params )

        if ( http_method in ( "POST", "PUT", "DELETE" ) and not
             headers.has_key( 'Content-Type' ) ):

            headers['Content-Type'] = 'application/json'

        headers['Accept'] = 'application/json'
        response, content = self.client.request(
                uri = uri,
                method = http_method,
                body = body,
                headers = headers
            )

        self.checkErrors( uri, response )

        return json.loads( str(content) )


    def createOrganisation( self, organisation_json ):
        """
        Create an Organisation object from a JSON object
        """
        return Organisation(
                trello_client = self,
                organisation_id = organisation_json['id'].encode('utf-8'),
                name = organisation_json['name'].encode( 'utf-8' )
            )


    def createBoard( self, board_json ):
        """
        Create Board object from a JSON object
        """
        return Board(
                trello_client = self,
                board_id = board_json['id'].encode('utf-8'),
                name = board_json['name'].encode( 'utf-8' )
            )


    def createList( self, list_json ):
        """
        Create List object from JSON object
        """
        return List(
                trello_client = self,
                list_id = list_json['id'].encode('utf-8'),
                name = list_json['name'].encode( 'utf-8' )
            )


    def createCard( self, card_json ):
        """
        Create a Card object from JSON object
        """
        return Card(
                trello_client = self,
                card_id = card_json['id'].encode('utf-8'),
                name = card_json['name'].encode( 'utf-8' )
            )


    def createChecklist( self, checklist_json ):
        """
        Create a Checklist object from JSON object
        """
        return Checklist(
                trello_client = self,
                checklist_id = checklist_json['id'].encode('utf-8'),
                name = checklist_json['name'].encode( 'utf-8' )
            )


    def createMember( self, member_json ):
        """
        Create a Member object from JSON object
        """
        return Member(
                trello_client = self,
                member_id = member_json['id'].encode('utf-8'),
                name = member_json['fullName'].encode( 'utf-8' )
            )


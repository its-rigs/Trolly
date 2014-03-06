'''
Created on 13 Nov 2012

@author: plish
'''

from trolly.trelloobject import TrelloObject


class Checklist( TrelloObject ):
    """
    Class representing a Trello Checklist
    """
    def __init__( self, trello_client, checklist_id, name = '' ):
        super( Checklist, self ).__init__( trello_client )

        self.id = checklist_id
        self.name = name

        self.base_uri = '/checklists/' + self.id


    def getChecklistInformation( self, query_params = {} ):
        """
        Get all information for this Checklist. Returns a dictionary of values.
        """
        return self.fetchJson(
                uri_path = self.base_uri,
                query_params = query_params
            )


    def getItems( self, query_params = {} ):
        """
        Get all the items for this checklist. Returns a list of dictionaries.
        Each dictionary has the values for an item.
        """
        return self.fetchJson(
                uri_path = self.base_uri + '/checkItems',
                query_params = query_params
            )


    def updateChecklist( self, name ):
        """
        Update the current checklist. Returns a new Checklist object.
        """
        checklist_json = self.fetchJson(
                uri_path = self.base_uri,
                http_method = 'PUT',
                query_params = { 'name': name }
            )

        return self.createChecklist( checklist_json )


    def addItem( self, query_params = {} ):
        """
        Add an item to this checklist. Returns a dictionary of values of new item.
        """
        return self.fetchJson(
                uri_path = self.base_uri + '/checkItems',
                http_method = 'POST',
                query_params = query_params
            )


    def removeItem( self, item_id ):
        """
        Deletes an item from this checklist.
        """
        return self.fetchJson(
                uri_path = self.base_uri + '/checkItems/' + item_id,
                http_method = 'DELETE'
            )

"""
Created on 13 Nov 2012

@author: plish
"""

from trolly.trelloobject import TrelloObject


class Checklist(TrelloObject):
    """
    Class representing a Trello Checklist
    """

    def __init__(self, trello_client, checklist_id, name=''):
        super(Checklist, self).__init__(trello_client)

        self.id = checklist_id
        self.name = name

        self.base_uri = '/checklists/' + self.id

    def get_checklist_information(self, query_params=None):
        """
        Get all information for this Checklist. Returns a dictionary of values.
        """
        return self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

    def get_items(self, query_params=None):
        """
        Get all the items for this checklist. Returns a list of dictionaries.
        Each dictionary has the values for an item.
        """
        return self.fetch_json(
            uri_path=self.base_uri + '/checkItems',
            query_params=query_params or {}
        )

    def update_checklist(self, name):
        """
        Update the current checklist. Returns a new Checklist object.
        """
        checklist_json = self.fetch_json(
            uri_path=self.base_uri,
            http_method='PUT',
            query_params={'name': name}
        )

        return self.create_checklist(checklist_json)

    def add_item(self, query_params=None):
        """
        Add an item to this checklist. Returns a dictionary of values of new item.
        """
        return self.fetch_json(
            uri_path=self.base_uri + '/checkItems',
            http_method='POST',
            query_params=query_params or {}
        )

    def remove_item(self, item_id):
        """
        Deletes an item from this checklist.
        """
        return self.fetch_json(
            uri_path=self.base_uri + '/checkItems/' + item_id,
            http_method='DELETE'
        )


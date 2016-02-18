from . import trelloobject


class Checklist(trelloobject.TrelloObject):

    '''
    Class representing a Trello Checklist
    '''

    def __init__(self, trello_client, checklist_id, name='', **kwargs):
        super(Checklist, self).__init__(trello_client, **kwargs)

        self.id = checklist_id
        self.name = name

        self.base_uri = '/checklists/' + self.id

    def get_checklist_information(self, query_params=None):
        '''
        Get all information for this Checklist. Returns a dictionary of values.
        '''
        # We don't use trelloobject.TrelloObject.get_checklist_json, because
        # that is meant to return lists of checklists.
        return self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

    def get_card(self):
        '''
        Get card this checklist is on.
        '''
        card_id = self.get_checklist_information().get('idCard', None)
        if card_id:
            return self.client.get_card(card_id)

    def get_items(self, query_params=None):
        '''
        Get all the items for this checklist. Returns a list of dictionaries.
        Each dictionary has the values for an item.
        '''
        return self.fetch_json(
            uri_path=self.base_uri + '/checkItems',
            query_params=query_params or {}
        )

    def get_item_objects(self, query_params=None):
        """
        Get the items for this checklist. Returns a list of ChecklistItem objects.
        """
        card = self.get_card()
        checklistitems_list = []
        for checklistitem_json in self.get_items(query_params):
            checklistitems_list.append(self.create_checklist_item(card.id, self.id, checklistitem_json))

        return checklistitems_list


    def update_checklist(self, name):
        '''
        Update the current checklist. Returns a new Checklist object.
        '''
        checklist_json = self.fetch_json(
            uri_path=self.base_uri,
            http_method='PUT',
            query_params={'name': name}
        )

        return self.create_checklist(checklist_json)

    def add_item(self, query_params=None):
        '''
        Add an item to this checklist. Returns a dictionary of values of new
        item.
        '''
        return self.fetch_json(
            uri_path=self.base_uri + '/checkItems',
            http_method='POST',
            query_params=query_params or {}
        )

    def remove_item(self, item_id):
        '''
        Deletes an item from this checklist.
        '''
        return self.fetch_json(
            uri_path=self.base_uri + '/checkItems/' + item_id,
            http_method='DELETE'
        )


class ChecklistItem(trelloobject.TrelloObject):
    """
    Class representing a Trello Checklist Item
    """
    def __init__(self, trello_client, card_id, checklist_id, checklistitem_id, name='', state='incomplete'):
        super(ChecklistItem, self).__init__(trello_client)

        self.idCard = card_id
        self.idChecklist = checklist_id
        self.id = checklistitem_id
        self.name = name
        self.state = (state == 'complete')

        self.base_uri = '/cards/' + self.idCard + '/checklist/' + self.idChecklist + '/checkItem/' + self.id


    def update_name( self, name ):
        """
        Rename the current checklist item. Returns a new ChecklistItem object.
        """
        checklistitem_json = self.fetch_json(
            uri_path = self.base_uri + '/name',
            http_method = 'PUT',
            query_params = {'value': name}
        )

        return self.create_checklist_item(self.idCard, self.idChecklist, checklistitem_json)


    def update_state(self, state):
        """
        Set the state of the current checklist item. Returns a new ChecklistItem object.
        """
        checklistitem_json = self.fetch_json(
            uri_path = self.base_uri + '/state',
            http_method = 'PUT',
            query_params = {'value': 'complete' if state else 'incomplete'}
        )

        return self.create_checklist_item(self.idCard, self.idChecklist, checklistitem_json)

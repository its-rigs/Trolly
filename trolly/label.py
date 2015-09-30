from . import trelloobject


class Label(trelloobject.TrelloObject):

    '''
    Class representing a Trello Label
    '''

    def __init__(self, trello_client, label_id, name='', **kwargs):
        super(Label, self).__init__(trello_client, **kwargs)

        self.id = label_id
        self.name = name

        self.base_uri = '/labels/' + self.id

    def get_label_information(self, query_params=None):
        '''
        Get all information for this Label. Returns a dictionary of values.
        '''
        return self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

    def get_items(self, query_params=None):
        '''
        Get all the items for this label. Returns a list of dictionaries.
        Each dictionary has the values for an item.
        '''
        return self.fetch_json(
            uri_path=self.base_uri + '/checkItems',
            query_params=query_params or {}
        )

    def update_label(self, name):
        '''
        Update the current label. Returns a new Label object.
        '''
        label_json = self.fetch_json(
            uri_path=self.base_uri,
            http_method='PUT',
            query_params={'name': name}
        )

        return self.create_label(label_json)


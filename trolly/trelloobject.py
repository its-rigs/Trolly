

class TrelloObject(object):

    '''
    This class is a base object that should be used by all trello objects;
    Board, List, Card, etc. It contains methods needed and used by all those
    objects and masks the client calls as methods belonging to the object.
    '''

    def __init__(self, trello_client, **kwargs):
        '''
        A Trello client, Oauth of HTTP client is required for each object.
        '''
        super(TrelloObject, self).__init__()

        self.client = trello_client
        self.data = kwargs.get('data', {})

    def __getattr__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            raise AttributeError('Unknown attribute %s' % key)

    def __repr__(self):
        return '<%s[%s] %s>' % (
            self.__class__.__name__,
            getattr(self, 'id', ''),
            getattr(self, 'name', ''),
        )

    def fetch_json(self, uri_path, http_method='GET', query_params=None,
                   body=None, headers=None):
        return self.client.fetch_json(
            uri_path=uri_path,
            http_method=http_method,
            query_params=query_params or {},
            body=body,
            headers=headers or {}
        )

    def get_organisations_json(self, base_uri):
        return self.fetch_json(base_uri + '/organizations')

    def get_boards_json(self, base_uri):
        return self.fetch_json(base_uri + '/boards')

    def get_labels_json(self, base_uri):
        return self.fetch_json(base_uri + '/labels')

    def get_board_json(self, base_uri):
        return self.fetch_json(base_uri + '/board')

    def get_lists_json(self, base_uri):
        return self.fetch_json(base_uri + '/lists')

    def get_list_json(self, base_uri):
        return self.fetch_json(base_uri + '/list')

    def get_cards_json(self, base_uri):
        return self.fetch_json(base_uri + '/cards')

    def get_checklist_json(self, base_uri):
        return self.fetch_json(base_uri + '/checklists')

    def get_members_json(self, base_uri):
        return self.fetch_json(base_uri + '/members')

    def create_organisation(self, organisation_json, **kwargs):
        '''
        Create an Organisation object from a JSON object

        Returns:
            Organisation: The organisation from the given `organisation_json`.
        '''
        return self.client.create_organisation(organisation_json, **kwargs)

    def create_board(self, board_json, **kwargs):
        '''
        Create Board object from a JSON object

        Returns:
            Board: The board from the given `board_json`.
        '''
        return self.client.create_board(board_json, **kwargs)

    def create_list(self, list_json, **kwargs):
        '''
        Create List object from JSON object

        Returns:
            List: The list from the given `list_json`.
        '''
        return self.client.create_list(list_json, **kwargs)

    def create_label(self, label_json, **kwargs):
        '''
        Create Label object from JSON object

        Returns:
            Label: The label from the given `label_json`.
        '''
        return self.client.create_label(label_json, **kwargs)

    def create_card(self, card_json, **kwargs):
        '''
        Create a Card object from JSON object

        Returns:
            Card: The card from the given `card_json`.
        '''
        return self.client.create_card(card_json, **kwargs)

    def create_checklist(self, checklist_json, **kwargs):
        '''
        Create a Checklist object from JSON object

        Returns:
            Checklist: The checklist from the given `checklist_json`.
        '''
        return self.client.create_checklist(checklist_json, **kwargs)

    def create_member(self, member_json, **kwargs):
        '''
        Create a Member object from JSON object

        Returns:
            Member: The member from the given `member_json`.
        '''
        return self.client.create_member(member_json, **kwargs)


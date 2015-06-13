
class TrelloObject(object):

    """
    This class is a base object that should be used by all trello objects;
    Board, List, Card, etc. It contains methods needed and used by all those
    objects and masks the client calls as methods belonging to the object.
    """

    def __init__(self, trello_client):
        """
        A Trello client, Oauth of HTTP client is required for each object.
        """
        super(TrelloObject, self).__init__()

        self.client = trello_client

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
        return self.fetch_json(base_uri + '/organization')

    def get_boards_json(self, base_uri):
        return self.fetch_json(base_uri + '/boards')

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
        return self.client.create_organisation(organisation_json, **kwargs)

    def create_board(self, board_json, **kwargs):
        return self.client.create_board(board_json, **kwargs)

    def create_list(self, list_json, **kwargs):
        return self.client.create_list(list_json, **kwargs)

    def create_card(self, card_json, **kwargs):
        return self.client.create_card(card_json, **kwargs)

    def create_checklist(self, checklist_json, **kwargs):
        return self.client.create_checklist(checklist_json, **kwargs)

    def create_member(self, member_json, **kwargs):
        return self.client.create_member(member_json, **kwargs)

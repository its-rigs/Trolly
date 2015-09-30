import mimetypes

from . import trelloobject


class Card(trelloobject.TrelloObject):

    '''
    Class representing a Trello Card
    '''

    def __init__(self, trello_client, card_id, name=''):

        super(Card, self).__init__(trello_client)

        self.id = card_id
        self.name = name

        self.base_uri = '/cards/' + self.id

    def get_card_information(self, query_params=None):
        '''
        Get information for this card. Returns a dictionary of values.
        '''
        return self.fetch_json(
            uri_path=self.base_uri,
            query_params=query_params or {}
        )

    def get_board(self, **query_params):
        '''
        Get board information for this card. Returns a Board object.

        Returns:
            Board: The board this card is attached to
        '''
        board_json = self.get_board_json(self.base_uri,
                                         query_params=query_params)
        return self.create_board(board_json)

    def get_list(self, **query_params):
        '''
        Get list information for this card. Returns a List object.

        Returns:
            List: The list this card is attached to
        '''
        list_json = self.get_list_json(self.base_uri,
                                       query_params=query_params)
        return self.create_list(list_json)

    def get_checklists(self, **query_params):
        '''
        Get the checklists for this card. Returns a list of Checklist objects.

        Returns:
            list(Checklist): The checklists attached to this card
        '''
        checklists = self.get_checklist_json(self.base_uri,
                                             query_params=query_params)

        checklists_list = []
        for checklist_json in checklists:
            checklists_list.append(self.create_checklist(checklist_json))

        return checklists_list

    def get_members(self, **query_params):
        '''
        Get all members attached to this card. Returns a list of Member
        objects.

        Returns:
            list(Member): The members attached to this card
        '''
        members = self.get_members_json(self.base_uri,
                                        query_params=query_params)

        members_list = []
        for member_json in members:
            members_list.append(self.create_member(member_json))

        return members_list

    def update_card(self, query_params=None):
        '''
        Update information for this card. Returns a new Card object.
        '''
        card_json = self.fetch_json(
            uri_path=self.base_uri,
            http_method='PUT',
            query_params=query_params or {}
        )

        return self.create_card(card_json)

    def add_comments(self, comment_text):
        '''
        Adds a comment to this card by the current user.
        '''
        return self.fetch_json(
            uri_path=self.base_uri + '/actions/comments',
            http_method='POST',
            query_params={'text': comment_text}
        )

    def add_attachment(self, filename, open_file):
        '''
        Adds an attachment to this card.
        '''
        fields = {
            'api_key': self.client.api_key,
            'token': self.client.user_auth_token
        }

        content_type, body = self.encode_multipart_formdata(
            fields=fields,
            filename=filename,
            file_values=open_file
        )

        return self.fetch_json(
            uri_path=self.base_uri + '/attachments',
            http_method='POST',
            body=body,
            headers={'Content-Type': content_type},
        )

    def add_checklists(self, query_params=None):
        '''
        Add a checklist to this card. Returns a Checklist object.
        '''
        checklist_json = self.fetch_json(
            uri_path=self.base_uri + '/checklists',
            http_method='POST',
            query_params=query_params or {}
        )

        return self.create_checklist(checklist_json)

    def add_labels(self, query_params=None):
        '''
        Add a label to this card.
        '''
        return self.fetch_json(
            uri_path=self.base_uri + '/labels',
            http_method='POST',
            query_params=query_params or {}
        )

    def add_member(self, member_id):
        '''
        Add a member to this card. Returns a list of Member objects.
        '''
        members = self.fetch_json(
            uri_path=self.base_uri + '/members',
            http_method='POST',
            query_params={'value': member_id}
        )

        members_list = []
        for member_json in members:
            members_list.append(self.create_member(member_json))

        return members_list

    def remove_member(self, member_id):
        '''
        Remove a member from this card.
        '''
        return self.fetch_json(
            uri_path=self.base_uri + '/members/' + member_id,
            http_method='DELETE'
        )

    def close_card(self):
        '''
        Close (archive) this card.
        '''
        return self.update_card({'closed': 'true'})

    def archive_card(self):
        '''
        Close (archive) this card. (Synonym for close_card().)
        '''
        return self.close_card()

    def delete_card(self):
        '''
        Permanently delete this card.
        '''
        return self.fetch_json(
            uri_path=self.base_uri,
            http_method='DELETE'
        )

    def encode_multipart_formdata(self, fields, filename, file_values):
        '''
        Encodes data to updload a file to Trello.
        Fields is a dictionary of api_key and token. Filename is the name of
        the file and file_values is the open(file).read() string.
        '''
        boundary = '----------Trello_Boundary_$'
        crlf = '\r\n'

        data = []

        for key in fields:
            data.append('--' + boundary)
            data.append('Content-Disposition: form-data; name="%s"' % key)
            data.append('')
            data.append(fields[key])

        data.append('--' + boundary)
        data.append(
            'Content-Disposition: form-data; name="file"; filename="%s"' %
            filename)
        data.append('Content-Type: %s' % self.get_content_type(filename))
        data.append('')
        data.append(file_values)

        data.append('--' + boundary + '--')
        data.append('')

        # Try and avoid the damn unicode errors
        data = [str(segment) for segment in data]

        body = crlf.join(data)
        content_type = 'multipart/form-data; boundary=%s' % boundary

        return content_type, body

    def get_content_type(self, filename):
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'

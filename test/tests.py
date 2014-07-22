'''
Created on 9 Nov 2012

@author: plish
'''

import unittest
import uuid

from trolly.client import Client
from trolly.organisation import Organisation
from trolly.board import Board
from trolly.list import List
from trolly.card import Card
from trolly.checklist import Checklist
from trolly.member import Member
from trolly import ResourceUnavailable


api_key = ''
user_auth_token = ''

organisation = ''
board_id = ''
list_id = ''
card_id = ''
checklist_id = ''
member_id = ''


class TrelloTests(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key, user_auth_token)
        self.org = Organisation(self.client, organisation)
        self.board = Board(self.client, board_id)
        self.list = List(self.client, list_id)
        self.card = Card(self.client, card_id)
        self.checklist = Checklist(self.client, checklist_id)
        self.member = Member(self.client, member_id)

    def tearDown(self):
        pass

    def test_org_01_getBoardInfo(self):
        result = self.org.getOrganisationInformation()
        self.assertIsNotNone(result, 'JSON was empty')

    def test_org_02_getBoards(self):
        for board in self.org.getBoards():
            self.assertIsNotNone(board.id, msg="ID has not been provided")
            self.assertIsNotNone(board.name, msg="Name has not been provided")

    def test_org_03_getMembers(self):
        for member in self.org.getMembers():
            self.assertIsNotNone(member.id, msg="ID has not been provided")
            self.assertIsNotNone(member.name, msg="Name has not been provided")

    def test_org_04_updateOrganisation(self):
        description = str(uuid.uuid1())
        new_organisation = self.org.updateOrganisation({'desc': description})
        new_description = new_organisation.getOrganisationInformation()['desc']

        self.assertEqual(description, new_description, msg="Descriptions don't match. Update Organisation didn't work!")

    def test_boa_01_getBoardInformation(self):
        result = self.board.getBoardInformation()
        self.assertIsNotNone(result, 'JSON was empty')

    def test_boa_02_getLists(self):
        for lis in self.board.getLists():
            self.assertIsNotNone(lis.id, msg="ID has not been provided")
            self.assertIsNotNone(lis.name, msg="Name has not been provided")

    def test_boa_03_getCards(self):
        for card in self.board.getCards():
            self.assertIsNotNone(card.id, msg="ID has not been provided")
            self.assertIsNotNone(card.name, msg="Name has not been provided")

    def test_boa_04_getCard(self):
        card = self.board.getCard(card_id)
        self.assertIsNotNone(card.id, msg="ID has not been provided")
        self.assertIsNotNone(card.name, msg="Name has not been provided")

    def test_boa_05_getMembers(self):
        for member in self.board.getMembers():
            self.assertIsNotNone(member.id, msg="ID has not been provided")
            self.assertIsNotNone(member.name, msg="Name has not been provided")

    def test_boa_06_getOrganisation(self):
        organisation = self.board.getOrganisation()
        self.assertIsNotNone(organisation.id, msg="ID has not been provided")
        self.assertIsNotNone(organisation.name, msg="Name has not been provided")

    def test_boa_07_updateBoard(self):
        description = str(uuid.uuid1())
        new_board = self.board.updateBoard({'desc': description})
        new_description = new_board.getBoardInformation()['desc']

        self.assertEqual(description, new_description, msg="Descriptions don't match. Update Board didn't work!")

    def test_boa_08_addList(self):
        name = str(uuid.uuid1())
        new_list = self.board.addList({'name': name})
        new_list_name = new_list.name

        self.assertEqual(name, new_list_name, msg="Names don't match. Add list didn't work!")

    def test_lis_01_getListInformation(self):
        result = self.list.getListInformation()
        self.assertIsNotNone(result, 'JSON was empty')

    def test_lis_02_getBoard(self):
        board = self.list.getBoard()
        self.assertIsNotNone(board.id, msg="ID has not been provided")
        self.assertIsNotNone(board.name, msg="Name has not been provided")

    def test_lis_03_getCards(self):
        for card in self.list.getCards():
            self.assertIsNotNone(card.id, msg="ID has not been provided")
            self.assertIsNotNone(card.name, msg="Name has not been provided")

    def test_lis_04_updateList(self):
        name = str(uuid.uuid1())
        new_list = self.list.updateList({'name': name})
        new_list_name = new_list.name

        self.assertEqual(name, new_list_name, msg="Names don't match. Update list didn't work!")

    def test_lis_05_addCard(self):
        name = str(uuid.uuid1())
        new_card = self.list.addCard({'name': name})
        new_card_name = new_card.name

        self.assertEqual(name, new_card_name, msg="Names don't match. Add card didn't work!")

    def test_car_01_getCardInformation(self):
        result = self.card.getCardInformation()
        self.assertIsNotNone(result, 'JSON was empty')

    def test_car_02_getBoard(self):
        board = self.card.getBoard()
        self.assertIsNotNone(board.id, msg="ID has not been provided")
        self.assertIsNotNone(board.name, msg="Name has not been provided")

    def test_car_03_getList(self):
        lis = self.card.getList()
        self.assertIsNotNone(lis.id, msg="ID has not been provided")
        self.assertIsNotNone(lis.name, msg="Name has not been provided")

    def test_car_04_getChecklists(self):
        for checklist in self.card.getChecklists():
            self.assertIsNotNone(checklist.id, msg="ID has not been provided")
            self.assertIsNotNone(checklist.name, msg="Name has not been provided")

    def test_car_05_getMembers(self):
        for member in self.card.getMembers():
            self.assertIsNotNone(member.id, msg="ID has not been provided")
            self.assertIsNotNone(member.name, msg="Name has not been provided")

    def test_car_06_updateCard(self):
        description = str(uuid.uuid1())
        new_card = self.card.updateCard({'desc': description})
        new_description = new_card.getCardInformation()['desc']

        self.assertEqual(description, new_description, msg="Descriptions don't match. Update Card didn't work!")

    def test_car_07_addComments(self):
        comment = str(uuid.uuid1())
        result = self.card.addComments(comment)
        new_comment = result['data']['text']

        self.assertEqual(comment, new_comment, msg="Comments don't match. Add comment didn't work!")

    def test_car_08_addAttachment(self):
        f = open('test/test.txt', 'r').read()
        result = self.card.addAttachment('text.txt', f)
        self.assertIsNotNone(result, "Got nothing back, doesn't look like it worked!")

    def test_car_09_addChecklists(self):
        name = str(uuid.uuid1())
        new_checklist = self.card.addChecklists({'name': name})
        new_checklist_name = new_checklist.name

        self.assertEqual(name, new_checklist_name, "Names don't match. Add Checklist failed!")

    def test_car_10_addLabels(self):
        try:
            label_colour = 'green'
            result = self.card.addLabels({'value': label_colour})

            found_label = False

            for label in result:
                if label['color'] == label_colour:
                    found_label = True

            self.assertTrue(found_label, "Label wasn't added!")

        except ResourceUnavailable:
            # Label already added
            pass


    def test_car_11_addMember(self):

        try:
            result = self.card.addMember(member_id)

            found_member = False

            for member in result:
                if member.id == member_id:
                    found_member = True

            self.assertTrue(found_member, "Member wasn't added to card!")

        except ResourceUnavailable:
            # Member is already on the card
            pass

    def test_car_12_removeMember(self):

        try:
            result = self.card.removeMember(member_id)

            self.assertIsNotNone(result, "JSON failure! Nothing was returned")

            for member in result:
                self.assertNotEqual(member['id'], member_id, "Member was not removed!")

        except ResourceUnavailable:
            # Member isn't attached to card
            pass

    def test_che_01_getChecklistInformation(self):
        result = self.checklist.getChecklistInformation()
        self.assertIsNotNone(result, 'JSON was empty')

    def test_che_02_getItems(self):
        result = self.checklist.getItems()
        self.assertIsNotNone(result, 'JSON was empty')

    def test_che_03_updateChecklist(self):
        name = str(uuid.uuid1())
        new_checklist = self.checklist.updateChecklist(name)
        new_name = new_checklist.name

        self.assertEqual(name, new_name, msg="Names don't match. Update didn't work!")

    def test_che_04_addItem(self):
        name = str(uuid.uuid1())
        result = self.checklist.addItem({'name': name})
        new_item_name = result[len(result) - 1]['name']

        self.assertEqual(name, new_item_name, "Names don't match! Add item failed")

    def test_che_05_removeItem(self):
        items = self.checklist.getItems()

        if len(items) > 0:
            item_id = items[0]['id']

            result = self.checklist.removeItem(item_id)
            self.assertIsNotNone(result, "JSON was empty!")

    def test_mem_01_getMemberInformation(self):
        result = self.member.getMemberInformation()
        self.assertIsNotNone(result, 'JSON was empty')

    def test_mem_02_getBoards(self):
        for board in self.member.getBoards():
            self.assertIsNotNone(board.id, msg="ID has not been provided")
            self.assertIsNotNone(board.name, msg="Name has not been provided")

    def test_mem_03_getCards(self):
        for cards in self.member.getCards():
            self.assertIsNotNone(cards.id, msg="ID has not been provided")
            self.assertIsNotNone(cards.name, msg="Name has not been provided")

if __name__ == '__main__':
    unittest.main()


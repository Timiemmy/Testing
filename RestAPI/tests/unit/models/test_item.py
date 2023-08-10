from unittest import TestCase
from RestAPI.models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('item', 99.99)
        self.assertEqual(item.name, 'item')
        self.assertEqual(item.price, 99.99)


    def test_json(self):
        item = ItemModel('item', 99.99)
        expected = {
            'name': 'item',
            'price': 99.99
        }

        self.assertEqual(item.json(), expected)
from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self):
        store = StoreModel('test')
        ## Test that when store is first created, items list is empty
        self.assertListEqual(store.items.all(), [],
                             "The store's items list length was not 0 even though no items were added")


    def test_crud(self):
        with self.app_context():
            store = StoreModel('test')

            self.assertIsNone(StoreModel.find_by_name('test'))

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('test'))

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('test'))

    def test_store_relationship(self): ## test rship with items - if you have an item, does it appear in the store
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 20, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(),1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_json(self):
        store = StoreModel('test')
        expected = {
            'id': None,
            'name': 'test',
            'items': [],
        }

        self.assertDictEqual(store.json(), expected)

    def test_json_with_item(self):
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 20, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'id': 1,
                'name': 'test',
                'items': [{
                    'name': 'test_item',
                    'price': 20,
                }],
            }

            self.assertDictEqual(store.json(), expected)



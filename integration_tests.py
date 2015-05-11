
import unittest
from operations import create, read, update, delete


class IntegrationTests(unittest.TestCase):
    def test_create(self):
        self.assertEqual(create('new_doc', '<asd>Test</asd>'), 'Document has not been added.')
        self.assertEqual(create('renewed', '<asd>Woo</asd>'), 'Document has been added.')

    def test_read(self):
        self.assertEqual(read('new_doc'), '<asd>Test</asd>')
        self.assertEqual(read('asd'), 'Document has not been read.')

    def test_update(self):
        self.assertEqual(update('doc', '<asd>Result</asd'), 'Document has not been updated.')
        self.assertEqual(update('renewed', '<asd>NewResult</asd>'), 'Document has not been updated.')

    def test_delete(self):
        self.assertEqual(delete('renewed'), 'Document has been deleted.')
        self.assertEqual(delete('sad'), 'Document has not been deleted.')
import unittest
from library_management import LibraryManagement


# Author: JAHANZEB NAWAZ
# Details: Unit tests for Test authors. it will add, update, view and delete the 
# authors in library management system.

class TestAuthors(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()


    # test case to add author.
    def test_add_author(self):
        data = self.set_author()
        expected_data = self.manager.authors[0]
        self.assertEqual(data, expected_data['name'])

    #function to populate author data in start for each test case.
    def set_author(self):
        name = "James"
        address = "Blekinge"
        data = self.manager.add_author(name, address)
        return data
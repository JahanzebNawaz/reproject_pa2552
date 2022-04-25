import unittest
from library_management import LibraryManagement


# Author: RAHUL
# Details: Unit tests for Testing books functionality. it will add, update, view and delete the
# books in library management system.

class TestBooks(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()

    # this test case will test the functionality for adding in the system.
    def test_add_book(self):
        data = self.set_book()
        expected = self.manager.books[0]
        self.assertEqual(data, expected['name'])

    # this function will populate the data in the storage.
    def set_book(self):
        name = "Rich dad Poor Dad"
        author = "James"
        copies = 20
        data = self.manager.add_book(name, author, copies)
        return data


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

    # this test cases first check the email books data.
    # then adds new data and checks again for data
    def test_check_book_exits(self):
        count = len(self.manager.books)
        self.assertEqual(count, 0)
        self.set_book()
        book_count =  len(self.manager.books)
        self.assertEqual(book_count, 1)

    # test case to check word counts for name of book
    # it checks if word count is greater than 0
    def test_count_words_of_book_name(self):
        data = self.set_book()
        self.assertGreater(len(data), 0)

    # this function will populate the data in the storage.
    def set_book(self):
        name = "Rich dad Poor Dad"
        author = "James"
        copies = 20
        data = self.manager.add_book(name, author, copies)
        return data


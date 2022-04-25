from ast import Subscript
import unittest
from library_management import LibraryManagement


# Author: JAHANZEB NAWAZ
# Details: Integration tests, that included func for the 
# Author, Book, Subscription and Subscriptions


class TestIntegrations(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()
    
    def test_integration(self):
        self.add_data_for_testing()
        subscription_obj = self.manager.subscriptions[0]
        self.assertIsNotNone(subscription_obj)
        book_on_index = self.manager.books[0]
        self.assertTrue(book_on_index)
        book_on_index = self.manager.books[subscription_obj['book']]
        self.assertTrue(book_on_index)

    # checks the data if greater than 0. 
    def test_check_data(self):
        self.add_data_for_testing()
        author = self.manager.authors
        self.assertGreaterEqual(len(author), 1)
        book = self.manager.books
        self.assertGreaterEqual(len(book), 1)
        subscriber = self.manager.subscribers
        self.assertGreaterEqual(len(subscriber), 1)
        subscription = self.manager.subscriptions
        self.assertGreaterEqual(len(subscription), 1)


    # function to add data for all codes. 
    def add_data_for_testing(self):
        author = self.set_author()
        book = self.set_book()
        subscriber = self.set_subscriber()
        subscription = self.add_subscription_data(23, 0, 30, 3)


    #function to populate author data in start for each test case.
    def set_author(self):
        name = "James"
        address = "Blekinge"
        data = self.manager.add_author(name, address)
        return data

    # function to populate book data for testing.
    def set_book(self):
        name = "Rich dad Poor Dad"
        author = "James"
        copies = 20
        data = self.manager.add_book(name, author, copies)
        return data
    
    # code to populate the library managemnet sys to be used.
    def set_subscriber(self):
        name = "John Willims"
        rollno = 23
        data = self.manager.add_subscriber(name, rollno)
        return data
    
    # function to add data for subscriptions.
    def add_subscription_data(self, rollno, book_index, amount, days):
         data = self.manager.add_subscriptions(rollno, book_index, amount, days)
         self.assertEqual(data, f"Book subscription added for rollno {rollno}")
         return data

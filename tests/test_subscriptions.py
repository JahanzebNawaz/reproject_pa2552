import unittest
from library_management import LibraryManagement


# Author: Lydia Sri Divya Dommeti
# Details: Unit tests for Testing subscription functionality. it will add, update, view and delete the
# subscription in library management system.

class TestSubscription(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()

    # function to add data for subscriptions.
    def add_subscription_data(self, rollno, book_index, amount, days):
         data = self.manager.add_subscriptions(rollno, book_index, amount, days)
         self.assertEqual(data, f"Book subscription added for rollno {rollno}")
         return data

    # this function will populate the data for the books.
    def set_book(self):
        name = "Rich dad Poor Dad"
        author = "James"
        copies = 20
        data = self.manager.add_book(name, author, copies)
        return data

    def test_add_subscription(self):
        data = self.add_subscription_data(23, 0, 20, 2)
        new_data = self.manager.subscriptions[0]
        self.assertEqual(new_data['student'], 23)
        self.assertEqual(new_data['book'], 0)
        self.assertEqual(new_data['amount'], 20)
        self.assertEqual(new_data['days'], 2)

    def test_integrated_test_for_book_and_subscription(self):
        book = self.set_book()
        book_index = 0
        subscription = self.add_subscription_data(23, book_index, 30, 3)
        subscription_obj = self.manager.subscriptions[0]
        self.assertEqual(book_index, subscription_obj['book'])
        get_book_on_index = self.manager.books[book_index]
        self.assertTrue(get_book_on_index)
        get_book_on_index = self.manager.books[subscription_obj['book']]
        self.assertTrue(get_book_on_index)


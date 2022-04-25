import unittest
from library_management import LibraryManagement


# Author: Lakshmi Bhargavi Rangavajjula
# Details: Unit tests for Testing subscriber functionality. it will add, update, view and delete the
# books in library management system.

class TestSubscriber(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()

    # test case for adding and testing the subscribers
    def test_add_subscriber(self):
        data = self.set_data()
        expected_data = self.manager.subscribers[0]
        self.assertEqual(data, expected_data['name'])
        self.assertTrue(expected_data['rollno'])

    def test_get_data_with_rollno(self):
        data = self.set_data()
        expected_data = self.manager.get_subscriber(23)
        self.assertEqual(expected_data['rollno'], 23)
        self.assertEqual(expected_data['name'], data)

    # code to populate the library managemnet sys to be used.
    def set_data(self):
        name = "John Willims"
        rollno = 23
        data = self.manager.add_subscriber(name, rollno)
        return data
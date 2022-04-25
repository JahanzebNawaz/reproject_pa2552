import unittest
from library_management import LibraryManagement


# Author: Lydia Sri Divya Dommeti
# Details: Unit tests for Testing subscription functionality. it will add, update, view and delete the
# subscription in library management system.

class TestSubscription(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()

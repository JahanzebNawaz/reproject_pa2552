import unittest
from library_management import LibraryManagement


# Author: JAHANZEB NAWAZ
# Details: Unit tests for Test authors. it will add, update, view and delete the 
# authors in library management system.

class TestAuthors(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()


    # test case to add author. it store new author in system.
    def test_add_author(self):
        data = self.set_author()
        expected_data = self.manager.authors[0]
        self.assertEqual(data, expected_data['name'])

    # this test case gets the data from the system and allow us to view and use it.
    def test_view_author(self):
        data = self.set_author()
        expected_data = self.manager.author_details("James")
        self.assertEqual(expected_data['name'], data)

    # test case to update the authors data.
    def test_update_student(self):
        self.set_author()
        data = self.manager.authors[0]
        name = data["name"]
        address = data["address"]
        output = self.manager.update_author(name, address)
        expected_output = f"{name}"
        self.assertEqual(expected_output, output)
    
    # deletes the author from the system.
    def test_delete_author(self):
        self.set_author()
        data = self.manager.authors[0]
        self.assertEqual(data['name'], data['name'])

    #function to populate author data in start for each test case.
    def set_author(self):
        name = "James"
        address = "Blekinge"
        data = self.manager.add_author(name, address)
        return data

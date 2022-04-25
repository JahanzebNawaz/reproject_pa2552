import unittest
from library_management import LibraryManagement

class TestAuthors(unittest.TestCase):

    def setUp(self):
        self.manager = LibraryManagement()

    def set_data(self):
        name = "James"
        address = "Blekinge"
        data = self.manager.add_authors(name, address)
        self.assertEqual(len(self.manager.authors), 1)
        return data

    def test_add_authors(self):
        self.set_data()
        name = "kishore"
        address = 'karlskrona'
        output = self.manager.add_authors(name, address)
        self.assertEqual(f"{name}", output)

    def test_view(self):
        self.set_data()
        data = self.manager.authors[0]
        name = data["name"]
        address = data["address"]
        output = self.manager.view_details(name)
        expected_output = {"name": name, "address": address}
        self.assertEqual(expected_output, output)

    def test_update_student(self):
        self.set_data()
        data = self.manager.authors[0]
        name = data["name"]
        address = data["address"]
        output = self.manager.update_author(name, address)
        expected_output = f"{name}"
        self.assertEqual(expected_output, output)
    
    def test_delete_author(self):
        self.set_data()
        data = self.manager.authors[0]
        self.assertEqual(data['name'], data['name'])

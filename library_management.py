import re


class LibraryManagement:
    """
    Library management System, a class to store data and then 
    it is used for the testing the functionality.
    """

    def __init__(self) -> None:
        self.authors = []
        self.books = []
        self.subscribers = []
        self.subscriptions = []
    

    # Author: Jahanzeb Nawaz
    # details: adding functionality for authors to be added in the system.
    def add_author(self, name, address):
        self.authors.append(
            {
                "name": name,
                "address": address
            }
        )
        return f"{name}"
    
    
    # Author Jahanzeb Nawaz
    # details adding more functionality to view a author from library mgmt system.
    # if there is no such record with the given name. it will return No data found.
    def author_details(self, name):
        for index in range(len(self.authors)):
            if self.authors[index]['name'] == name:
                return self.authors[index]
        return "No data found"
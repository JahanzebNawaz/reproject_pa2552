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
        # return f"{name}"
    
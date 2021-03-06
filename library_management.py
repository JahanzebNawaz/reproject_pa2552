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

    # Author: Jahanzeb Nawaz
    # Details: this funcionality is used to update the author record.
    def update_author(self, name, address):
        for index in range(len(self.authors)):
            if self.authors[index]["name"] == name:
                self.authors[index] = {"name": name, "address":address}
                return f"{name}"
        return "No data found"

    # Author: Jahanzeb Nawaz
    # Details: this funcionality is used to delete the author record.
    def delete_author(self, name):
        for index in range(len(self.authors)):
            if self.authors[index]["name"] == name:
                self.authors.pop(index)
                return f"{name}"
        return "No data found"

    # Author Rahul
    # details: code to add new book in the system
    def add_book(self, name, author, copies):
        self.books.append({
            "name": name,
            "author": author,
            "copies": copies
        })
        return f"{name}"

    # Author: Lakshmi
    # details: adding function for the subscribers to be added in the system
    # and returns the name of the subscriber
    def add_subscriber(self, name, rollno):
        self.subscribers.append({
            "name": name,
            "rollno": rollno
        })
        return f"{name}"

    # Author: Lakshmi
    # this function returns the data of the existing subscriber incase it does not match with any
    # rollno it return no data found.
    def get_subscriber(self, rollno):
        for index in range(len(self.subscribers)):
            if self.subscribers[index]["rollno"] == rollno:
                return self.subscribers[index]
        return "No data Found"

    # Author: Lakshmi
    # details: function to delete subscriber from the subscribers list. using the
    # roll no
    def delete_subscriber(self, rollno):
        for index in range(len(self.subscribers)):
            if self.subscribers[index]["rollno"] == rollno:
                self.subscribers.pop(index)
                return f"{rollno} rollno deleted"
        return "No data Found"

    # Author: Divya
    # Details: a function to add subscriptions in the library system.
    def add_subscriptions(self, rollno, book_index, amount, days):
        self.subscriptions.append(
            {
                "student": rollno,
                "book": book_index,
                "amount": amount,
                "days": days
            }
        )
        return f"Book subscription added for rollno {rollno}"

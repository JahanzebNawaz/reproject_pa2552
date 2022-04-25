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
    

    def add_authors(self, name, address):
        self.authors.append(
            {
                "name":name,
                "address":address
            }
        )
        return f"{name}"

    def view_details(self, name):
        for index in range(len(self.authors)):
            if self.authors[index]["name"] == name:
                return self.authors[index]
        else:
            return "No data found"

    def update_author(self, name, address):
        for index in range(len(self.authors)):
            if self.authors[index]["name"] == name:
                self.authors[index] = {"name": name, "address":address}
                return f"{name}"
        else:
            return "No data found"

    def delete_author(self, name):
        for index in range(len(self.authors)):
            if self.authors[index]["name"] == name:
                self.authors.pop(index)
                return f"{name}"
        else:
            return "No data found"
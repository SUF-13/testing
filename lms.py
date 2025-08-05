class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book}' added to the system.")

    def add_user(self, user):
        self.users.append(user)
        print(f"User '{user}' added to the system.")

    def list_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available books:")
            for book in self.books:
                print(f"- {book}")

    def list_users(self):
        if not self.users:
            print("No users registered.")
        else:
            print("Registered users:")
            for user in self.users:
                print(f"- {user}")
        print("End of user list.")
        print("Total users:", len(self.users))
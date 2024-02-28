

class User:

    def __init__(self, username):

        self.__username = username
        self.books_list = []

    def get_username(self):

        return self.__username

    def get_book_list(self):

        return self.books_list

    def add_book(self, new_book):

        self.books_list.append(new_book)

    def remove_book(self, delete_book):

        self.books_list.remove(delete_book)

    # jak = User()
    #
    # jak.set_username('jak1715')
    #
    # print(jak.get_username())
    #
    # jak.add_book(britney_book)
    # jak.add_book(midnight_book)
    #
    # for book in jak.books_list:
    #     print(book)

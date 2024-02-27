# Class names always start with a capital letter
class Book:
    # instance_count variable stores how many instances of the Book class exists
    instance_count = 0

    # init is a special method called a CONSTRUCTOR that initializes the object's attributes
    # initial values are passed to this init method and stored as attributes
    # values will be accessed by other methods later on
    # self refers to the current instance of the class
    # self is used to access variables and methods associated with the current instance
    def __init__(self, title, author, genre):
        # accessing the main_title attribute of the current instance of the class
        self._main_title = title
        self._author_name = author
        self._which_genre = genre
        # accessing the instance_count variable of the Book class and adding 1 to its value
        Book.instance_count += 1

    def get_info(self):
        info = {'Title': self._main_title}
        return info

    # del method is called when an object is about to be destroyed
    def __del__(self):
        # accessing the instance_count variable of the Book class and subtracting 1 from its value
        Book.instance_count -= 1



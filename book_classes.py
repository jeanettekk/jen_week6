# Simple Book Tracker for Kids

# abc module helps you define an abstract base class (ABC)
# An ABC is a class that is meant to be subclassed, but not instantiated directly
# ABC defines a common interface that subclasses must follow by implementing certain methods
from abc import ABC, abstractmethod

# Importing the datetime class from the datetime module to create an instance in two methods
from datetime import datetime


# Class names always start with a capital letter
# class statement defines a new class, BookTracker
# ABC indicates this is an abstract class, defining a common interface that subclasses must implement
class BookTracker(ABC):

    # @abstractmethod decorator marks a method as abstract within an abstract base class
    # @abstractmethod indicates subclasses must provide their own implementations of this method
    # track_progress method should return current info about book reading progress, how each subclass uniquely tracks it
    @abstractmethod
    def track_progress(self):
        # pass is a placeholder indicating that this method has no implementation in the ABC
        pass

    # award_badge method returns a string, awarding a badge, after a specific amount of reading progress is made.
    @abstractmethod
    def award_badge(self):
        # pass is a placeholder indicating that this method has no implementation in the ABC
        pass


# class statement defines a subclass, DatesLevel, and inherits the BookTracker abstract class
class DatesLevel(BookTracker):
    # instance_count variable stores how many instances of the DatesLevel class exists
    instance_count = 0

    # init is a special method called a CONSTRUCTOR that initializes the object's attributes
    # initial values are passed to this constructor and stored as attributes
    # values will be accessed by other methods later on
    # self refers to the current instance of this class
    # self is used to access variables and methods associated with the current instance
    def __init__(self, title, author, genre):

        # Encapsulation - restricting access to certain parts of the class
        # Encapsulation provides data protection and prevents direct manipulation of certain parts of the class

        # adding an _ to an attribute name means it is 'protected'
        # _ cannot be directly assigned a value, it has to be accessed through a method or subclasses
        self._book_title = title
        self._author_name = author
        self._which_genre = genre
        # Initially assigning None to these attributes
        # Their values can only be assigned through methods
        self._start_date = None
        self._end_date = None
        self._read_period = None

        # accessing the instance_count variable of the Book class and adding 1 to its value
        DatesLevel.instance_count += 1

    # def defines the set_start_date method with 4 parameters, 3 parameters have a default value of None
    def set_start_date(self, day=None, month=None, year=None):

        # if the default value, None, is used, execute this code
        if None in [day, month, year]:
            # now() method returns a datetime object of the datetime class
            # datetime object represents current date and time and assigns it to current_date variable
            current_date = datetime.now()

            # date() method extracts only the date from current_date object
            # str() function converts the object into a string
            # split method converts the string into a list, - indicates where to separate the items
            # new list is stored in self._start_date variable
            self._start_date = str(current_date.date()).split('-')
            # Reassigns a new order for the date items of the list using their index (day, month, year)
            self._start_date = [self._start_date[2], self._start_date[1], self._start_date[0]]

        # if arguments are passed to this method, numbers representing dates, execute this code
        else:
            # f string converts day, month, year to a string
            # split method converts string to a list, separating items by - and assigns it to self._start_date variable
            self._start_date = f'{day}-{month}-{year}'.split('-')

    # def statement defines the get_start_date method
    def get_start_date(self):

        # return statement returns the self._start_date attribute
        return self._start_date

    # def statement defines the set_start_date method with 4 parameters, 3 parameters have a default value of None
    def set_end_date(self, day=None, month=None, year=None):

        # if the default value, None, is used, execute this code
        if None in [day, month, year]:
            # now() method returns a datetime object of the datetime class
            # datetime object represents current date and time and assigns it to current_date variable
            current_date = datetime.now()
            # date() method extracts only the date from current_date object
            # str() function converts the object into a string
            # split method converts the string into a list, - indicates where to separate the items
            # new list is stored in self._end_date variable
            self._end_date = str(current_date.date()).split('-')
            # Reassigns a new order for the date items of the list using their index (day, month, year)
            self._end_date = [self._end_date[2], self._end_date[1], self._end_date[0]]

        # if arguments are passed to this method, numbers representing dates, execute this code
        else:
            # f string converts day, month, year to a string
            # split method converts string to a list, separating items by - and assigns it to self._start_date variable
            self._end_date = f'{day}-{month}-{year}'.split('-')

    # def statement defines the get_end_date method
    def get_end_date(self):

        # return statement returns the self._end_date attribute
        return self._end_date

    # def statement defines track_progress method, inherited from BookTracker, the abstract base class
    def track_progress(self):

        # if the self._end_date attribute has a value of None, execute this code
        if self._end_date is None:
            # return statement returns string informing the user book is not finished
            return 'Book is not yet finished'

        # if self._end_date has a value other than None, execute this code
        else:
            # int() function converts each item to an integer
            # Instantiated 2 datetime objects of the datetime class to represent the start date and end date
            __start_date = datetime(int(self._start_date[2]), int(self._start_date[1]), int(self._start_date[0]))
            __end_date = datetime(int(self._end_date[2]), int(self._end_date[1]), int(self._end_date[0]))

            # the difference is returned between the two dates
            # days attribute extracts the number of days from the objects and assigns it to self._read_period
            self._read_period = (__end_date - __start_date).days

            # return statement returns a string, informing the user of the number of days it took to read a book
            return f'Finished reading in {self._read_period} days'

    # def statement defines the award_badge method, inherited from the BookTracker abstract base class
    def award_badge(self):
        # if self._end_date does NOT contain the value of None, execute this code
        if self._end_date is not None:

            # returns a string informing the user they finished the book and awards a book badge.
            return f'You finished {self._book_title} - Here\'s a BOOK Badge!'

    # Polymorphism - Operator overloading
    # Customising the behaviour of predefined operators or special methods when they are applied to instances of a class
    def __str__(self):
        # Assigned the value of None to variable __end, a private variable
        __end = None

        # if self._end_date does NOT contain the value of None, execute this code
        if self._end_date is not None:

            # join method concatenates the items in _end_date and separates them with / in between
            __end = '/'.join(self._end_date)

        # returns a string containing info about the current instance with end date's value as 'None'
        return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nStart: '
                f'{self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd: {__end}\n'
                f'{self.track_progress()}')

    # del method is called when an object is about to be destroyed
    def __del__(self):
        # accessing the instance_count variable of the DatesLevel class and subtracting 1 from its value
        DatesLevel.instance_count -= 1


# SUB CLASS ------------------------------------------------------------------------------------------------------------
# Inheritance - inherits Book class' attributes & methods
# This is multi-level inheritance, PagesLevel subclass inherits the DatesLevel subclass, including the ABC
# There is also single, multiple inheritance & hierarchical inheritance
class PagesLevel(DatesLevel):
    # def is defining the constructor for this class with 5 parameters
    def __init__(self, title, author, genre, pages):
        # super() initializes attributes inherited from the DatesLevel class
        super().__init__(title, author, genre)
        self._pages_count = pages
        self.pages_finished = 0
        # dunderscore means this is 'private' and should only be accessed within this class, not subclasses
        # percentage attribute tracks percentage of book read and is used for the award_badge method later
        self.__percentage = 0

    # Polymorphism - method overriding
    # Customising the behaviour of the set_end_date method, inherited the super class, DatesLevel
    def set_end_date(self, day=None, month=None, year=None):
        # CUSTOM BEHAVIOUR
        # assign the value of self._pages_count to self.pages_finished to indicate the book is finished
        self.pages_finished = self._pages_count

        # if the value of None is in day, month and year, execute this code
        if None in [day, month, year]:
            # now() method returns a datetime object of the datetime class
            # datetime object represents current date and time and assigns it to current_date variable
            current_date = datetime.now()
            # date() method extracts only the date from current_date object
            # str() function converts the object into a string
            # split method converts the string into a list, - indicates where to separate the items
            # new list is stored in self._end_date variable
            self._end_date = str(current_date.date()).split('-')
            self._end_date = [self._end_date[2], self._end_date[1], self._end_date[0]]
        else:
            # f string converts day, month, year to a string
            # split method converts string to a list, separating items by - and assigns it to self._start_date variable
            self._end_date = f'{day}-{month}-{year}'.split('-')

    # def statement defines the set_pages method, a setter, with two parameters
    def set_pages(self, pages):
        # if the self.pages_finished value is greater or equal to self._pages_count, execute this code
        if self.pages_finished >= self._pages_count:

            # prints a string about max pages
            print('Maximum book pages reached.')

            # Assign the value of self._pages_count to self.pages_finished
            self.pages_finished = self._pages_count

        # else if self.pages_finished is less than self._pages_count, execute this code
        else:
            # assigns the value of pages to self.pages_finished
            self.pages_finished = pages

    # def statement defines track_progress method, inherited from BookTracker, the abstract base class
    def track_progress(self):
        # equation returns the percentage finished and round() returns a rounded number, assigns it to self.__percentage
        self.__percentage = round((self.pages_finished / self._pages_count) * 100)

        # returns a string about percentage of pages finished
        return f'{self._book_title}: {self.__percentage}% Done\n{self.pages_finished}/{self._pages_count} pages finished'

    # def statement defines the award_badge method, inherited from the BookTracker abstract base class
    def award_badge(self):
        # if self._end_date does not contain the value of None, execute this code
        if self._end_date is not None:

            # returns a string about a badge award
            return f'You finished {self._book_title} - Here\'s a BOOK Badge!'

        # else if self.__percentage is between the range of 25-51, execute this code
        elif self.__percentage in range(25, 51):

            # returns a string about a bronze star award
            return f'You finished 1/4 of {self._book_title} so far! Here\'s a BRONZE Star!'

        # else if self.__percentage is between the range of 50-76, execute this code
        elif self.__percentage in range(50, 76):

            # returns a string about a silver star award
            return f'You finished 1/2 of {self._book_title} so far! Here\'s a SILVER Star!'

        # else if self.__percentage value is above 75, execute this code
        else:
            # returns a string about a gold star award
            return f'You finished 3/4 of {self._book_title}. So close! Here\'s a GOLD Star!'

    # Polymorphism - Operator overloading
    # Customising the behaviour of predefined operators or special methods when they are applied to instances of a class
    def __str__(self):
        # Assigned the value of None to variable __end, a private variable
        __end = None
        # if self._end_date does NOT contain the value of None, execute this code
        if self._end_date is not None:
            __end = '/'.join(self._end_date)

        # returns a string containing info about the current instance with end date's value as 'None'
        return (f'Book Title: {self._book_title}\nAuthor: {self._author_name}\nGenre: {self._which_genre}\nPages: '
                f'{self._pages_count}\nStart: {self._start_date[0]}/{self._start_date[1]}/{self._start_date[2]}\nEnd:'
                f' {__end}\n{self.track_progress()}')


if __name__ == '__main__':
    # OBJECT 1 - TESTING DATES & OBJECT INSTANTIATION ------------------------------------------------------------------
    # Passing string arguments to become attributes & instantiating the midnight_book object of the Book class
    midnight_book = DatesLevel('The Midnight Library', 'Matt Haig', 'Fiction')

    # Invoking the set_start_date method of the Book class, setting a date for when the book started
    # date is stored in the _start_date attribute of the midnight_book object
    midnight_book.set_start_date(12, 5, 2023)

    # Invoking the set_end_date method of the Book class
    # When no arguments are passed, today's date is assigned to the _end_date attribute of the midnight_book object
    midnight_book.set_end_date()

    print(midnight_book, '\n')

    # OBJECT 2 - TESTING PAGES -----------------------------------------------------------------------------------------
    britney_book = PagesLevel('The Woman in Me', 'Britney Spears', 'Memoir', 287)

    britney_book.set_start_date(29, 9, 2023)

    britney_book.set_pages(100)
    print(britney_book, '\n')

    # BOOK TRACKING & AWARDS -------------------------------------------------------------------------------------------
    # DateLevel & PagesLevel
    print(midnight_book.track_progress(), '\n')
    print(britney_book.track_progress(), '\n')

    # DateLevel & PagesLevel
    print(midnight_book.award_badge())
    print(britney_book.award_badge())

    # INSTANCE COUNT ---------------------------------------------------------------------------------------------------
    print(f'\nInstance Count: {britney_book.instance_count}')

    del britney_book

    print(f'Instance Count: {midnight_book.instance_count} (deleted 1 instance)')

# duck typing - using a method interchangeably with other objects

# class is our capsule
# it's a collection of attributes and methods
class Account:
    # numCreated keeps track of how many instances of the class exists
    # Creating a new instance of a class is also creating a new object based on the class's blueprint
    numCreated = 0

    # special method called the CONSTRUCTOR
    # a constructor method is used to get your object ready to be used
    # _balance is an attribute, a piece of data
    # dunderscore means 'really special' variable
    def __init__(self, initial_amount, firstname, lastname):
        # _ in balance means semi-private
        self._balance = initial_amount
        self.first_name = firstname
        # __ also means PRIVATE - KEEP OUT, dunderscores mean, there be dragons!
        self.__last_name = lastname
        Account.numCreated += 1

    # return is implicit
    # behaviour method
    def deposit(self, amount):
        self._balance += amount

    # self points to an object, an object pointer
    # in JavaScript, 'self' is 'this'
    # all object oriented languages have a version of 'self'
    def withdraw(self, amount):
        self._balance -= amount

    # Java call this a getter
    # Java uses these to retrieve attribute values
    def getbalance(self):
        return self._balance

    # create a getter method to retrieve the first_name attribute
    # getters READ or RETURN something
    def get_firstname(self):
        return self.first_name

    def get_lastname(self):
        return self.__last_name

    # setters WRITE and do NOT return/read values
    # setters have parameters
    # setters modify incoming data
    # setters often contain if statements
    def set_lastname(self, new_lastname):

        self.__last_name = new_lastname

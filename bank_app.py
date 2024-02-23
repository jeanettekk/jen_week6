from account import Account
# class starts with a capital

# dir will show functionality of Account class
# print(dir(Account))

# instantiation - How to do it!
# this is when we create objects based on classes

# Step 1. Construct an object, gives a hexidecimal address of the block of memory with Lisa's bank account
lisa_account = Account(100, 'Lisa', 'Simpson')

# Step 2. refer to the variable that refers to the object in memory
# getbalance is a getter method, you don't pass parameters in these
lisa_balance = lisa_account.getbalance()

print(f'${lisa_balance}')

# add some cash to Lisa's account
# OOP notation: object.method()

lisa_account.deposit(20)
lisa_balance = lisa_account.getbalance()
print(f'${lisa_balance}')

# This didn't work at first because the attribute name was private with __
# first = lisa_account.get_lastname()
# print(first)

# Encapsulation - hiding stuff is good! Keeps other devs out, 'don't poke in my code'
# Gives us a layer of abstraction
# We created a getter method for the private attribute
lastname = lisa_account.get_lastname()
print(lastname)

lisa_account.set_lastname('Van Houten')
# setters modify the incoming data
print(f"Lisa's old last name was {lastname} and her new lastname is {lisa_account.get_lastname()}")
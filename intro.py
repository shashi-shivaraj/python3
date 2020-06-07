# File to learn basic concepts in python3

from datetime import datetime, timedelta

# print to console
print("Welcome")

# read input from user
inp = input("type something\n")
print("You typed : " + inp)

# strings
name = "shashi"
surname = "shivaraju"
print("hello " + name.capitalize() + ' ' + surname.upper())
# format holders
print("hello {} {} ".format(name.capitalize(), surname.upper()))
print("hello {0} {1} ".format(name.capitalize(), surname.upper()))
print(f"hello {name.capitalize()} {surname.upper()}")

# numberic datatypes
pi = 3.142
print(pi)
out = 2+8
print(float(out))

# exponent is **
print("2 ^ 4 is " + str(2 ** 4))

# dates
today = datetime.now()
print(" today time is " + str(today))
yesterday = today - timedelta(days=1)
print(" yesterday time is " + str(yesterday))

birth = input("enter your birth day in dd/mm/yyyy")
birth_day = datetime.strptime(birth, "%d/%m/%Y")
print("bd = " + str(birth_day))

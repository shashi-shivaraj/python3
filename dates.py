# dates
from datetime import datetime, timedelta

today = datetime.now()
print(" today time is " + str(today))
yesterday = today - timedelta(days=1)
print(" yesterday time is " + str(yesterday))

birth = input("enter your birth day in dd/mm/yyyy")
birth_day = datetime.strptime(birth, "%d/%m/%Y")
print("bd = " + str(birth_day))

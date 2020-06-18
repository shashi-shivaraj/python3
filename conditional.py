# conditional statements

price = input("enter the cost\n")

price = float(price)

# if else
if price >= 1.00:
    tax = 0.07
else:
    tax = 0

print("tax rate is : " + str(tax))


# nested if elif else
country = input("enter the country \n")

if country.lower() == 'india' or country.lower() == 'bharat':
    print("you are an indian")
    state = input("enter your state \n")
    if state.lower() == 'karnataka':
        print("you are a kannadiga")
elif country.lower() in ('usa', 'canada'):
    print("you are american/canadian")
else:
    print("your country is unknown")

age = int(input("enter your age \n"))

# nested if
if age > 20 and age < 30:
    print("your age qualifies")
else:
    print("your age does not qualify")

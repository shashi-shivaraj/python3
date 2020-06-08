# file to demo error handling
x = 42
y = 0

try:
    print(x/y)
except ZeroDivisionError as e:
    print("operation not allowed")
else:
    print("error occured")
finally:
    print("code cleanup")

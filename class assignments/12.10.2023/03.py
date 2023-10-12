# Write a program that asks the user to enter their age as an integer. If the user enters
# a non-integer value, they should handle the `ValueError` and raise a custom
# `InvalidAgeError` exception. They should provide an informative error message with
# the exception.

class InvalidAgeError(ValueError):
    pass


try:
    age = int(input("enter your age : "))
    if age < 0:
        raise InvalidAgeError("enter positive number")
except InvalidAgeError as i:
    print("Error Message : %s" % i)
except ValueError:
    print("enter only integer do not enter characters")
else:
    print("your age is : ", age)









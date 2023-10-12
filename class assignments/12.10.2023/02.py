# Write a program to perform an operation between two data types that are not
# compatible (e.g., adding a string and an integer). The program need to handle
# theTypeError` and print a suitable error message.

try:
    a = int(input("enter a value"))
    b = input("enter a value")
    c = a + b
except TypeError:
    print("we cannot able to add string and integer datatypes")
else:
    print("the addition is : ", c)





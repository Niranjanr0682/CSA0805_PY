# write program to takes two numbers as input from the user, and then handles the
# ZeroDivisionError. if the second number is zero. The code should provide a
# meaningful error message.
try:
    a = int(input("enter 1st value : "))
    b = int(input("enter 2nd value : "))
    d = a / b
    print("the division of the given number is : ", d)
except ZeroDivisionError:
    print("you have entered invalid integer value\n "
          "nothing can divided by zero.")

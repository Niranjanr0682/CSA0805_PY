# Write a program that defines functions for basic mathematical operations
# (addition, subtraction, multiplication, and division). Allow the user to
# input two numbers and select an operation to perform. Use separate functions
# for each operation.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."


while True:
    print("____menu____"
          "\na. Addition"
          "\nb. Subtraction"
          "\nc. Multiplication"
          "\nd. Division"
          "\ne. Exit")
    option = input("Enter option : ")
    if option == 'e':
        break
    if option in ('a', 'b', 'c', 'd'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if option == 'a':
                print("Result:", add(num1, num2))
            elif option == 'b':
                print("Result:", subtract(num1, num2))
            elif option == 'c':
                print("Result:", multiply(num1, num2))
            elif option == 'd':
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Please enter valid numbers.")
    else:
        print("Invalid input. Please enter a valid option.")

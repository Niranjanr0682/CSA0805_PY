# Write a program that takes user input for a number and handles exceptions if
# the input is not a valid number.

user_input = input("Enter an integer number: ")

try:
    number = int(user_input)
except ValueError:
    print("Invalid input. Please enter a valid integer number.")
else:
    print(f"You entered {number}.")
finally:
    print("bye")

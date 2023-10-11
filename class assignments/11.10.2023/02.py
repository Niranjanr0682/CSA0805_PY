# Write a program that asks the user to enter numbers one by one. Continue reading
# numbers until the user enters -1. Calculate and print the sum of all the entered
# numbers (excluding -1).
number = int(input("Enter a number: "))
sum = 0
while number != -1:
    sum += number
    number = int(input("Enter a number: "))
print("the sum of all entered number is : ", sum)



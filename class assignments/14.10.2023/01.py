# Write a function that takes a list of numbers and returns a tuple containing the sum
# and average of the numbers.

def sum_and_average(numbers):
    sum = 0
    for number in numbers:
        sum += number

    average = sum / len(numbers)

    return sum, average


try:
    list_numbers = []
    length = int(input("enter the range of list : "))

    for i in range(length):
        ele = int(input(f"enter value {i + 1}: "))
        list_numbers.append(ele)
    add, avg = sum_and_average(list_numbers)

    print(add)
    print(avg)

except ValueError:
    print("invalid character ...")

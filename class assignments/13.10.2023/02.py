# Write a program that defines functions to find the sum, maximum and minimum
#     values in a list of numbers.

def find_sum(numbers):
    return sum(numbers)


def find_max(numbers):
    return max(numbers)


def find_min(numbers):
    return min(numbers)


numbers_list = []
length = int(input("enter the length of the list : "))
for i in range(length):
    element = int(input("enter value : "))
    numbers_list.append(element)

total_sum = find_sum(numbers_list)
max_value = find_max(numbers_list)
min_value = find_min(numbers_list)
print("List of numbers:", numbers_list)
print("Sum:", total_sum)
print("Maximum value:", max_value)
print("Minimum value:", min_value)

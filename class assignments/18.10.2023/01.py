def add_positive(numbers):
    total_sum = 0
    for num in numbers:
        if num > 0:
            total_sum += num
    return total_sum


X = [1, 2, 3, -4, 5, 6, -7, 8, 9, 10, -3]
add = add_positive(X)
print("Sum of positive numbers:", add)


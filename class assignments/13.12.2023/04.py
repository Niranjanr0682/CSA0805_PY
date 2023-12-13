# Write a function to check if a given number is prime.

import math


def is_prime(n, i=2):
    if n < 2:
        return False
    if i > math.sqrt(n):
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)


num = int(input("enter number to check for prime number :"))
if is_prime(num):
    print(f"the given number {num} is prime.")
else:
    print(f"the given number {num} is not prime.")

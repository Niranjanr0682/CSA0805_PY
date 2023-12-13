# Write a function to reverse a string.

def reverse(s):
    return s[::-1]


string = input("enter a string to reverse : ")
print("the reversed string is :\n", reverse(string))

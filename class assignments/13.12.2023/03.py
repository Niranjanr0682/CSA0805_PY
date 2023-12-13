# Write a function to check if a given string is a palindrome.

def is_palindrome(s):
    s = s.lower().replace(' ', '')
    return s == s[::- 1]


string = (input("enter string to check for palindrome :"))

if is_palindrome(string):
    print(f"the given string {string} is palindrome")
else:
    print(f"the given string {string} is not palindrome")

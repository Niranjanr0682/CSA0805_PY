# Write a program that defines function to;
#             a. count the number of vowels in a given string,
#             b. length of the string
#             c. to reverse the string.
# Test these functions.

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


def calculate_length(s):
    return len(s)


def reverse_string(s):
    return s[::-1]


input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)
string_length = calculate_length(input_string)
print("Length of the string:", string_length)

reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)

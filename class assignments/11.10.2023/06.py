# Create a program that takes a user's input string and performs following string operations.
# The program should ask the user to input a string, then let user select an operation to
# manipulate the string and display the outcome at the end of program.
# String operation:
# a. Capitalize the string
# b. Reverse the string
# c. Display the length of the string
# d. Find a specific word in a string
# e. Replace a specific word with a new word
# f. Extend the string

s = input("enter a sentence : ")
print("----menu----"
      "\na. Capitalize the string"
      "\nb. Reverse the string"
      "\nc. Display the length of the string"
      "\nd. Find a specific word in string"
      "\ne. Replace a specific word with a new word"
      "\nf. Extend the string")
op = input("enter your option : ")
if op == 'a':
    print("the Capitalized string :\n", s.upper())
elif op == 'b':
    print("the reversed string :\n", s[::-1])
elif op == 'c':
    print("the length of the given string is : ", len(s))
elif op == 'd':
    sw = input("enter a word to find : ")
    print("the word found at index : ", s.find(sw))
elif op == 'e':
    sw = input("enter the word to change : ")
    nw = input("enter new word to change : ")
    ns = s.replace(sw, nw)
    print("given string    :%s\n "
          "modified string :%s" % (s, ns))
elif op == 'f':
    e = input("enter a new string to extend the previous : \n")
    s += e
    print("the extended string is :\n",s)
else:
    print("enter a valid option....")

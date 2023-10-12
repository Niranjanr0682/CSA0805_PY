# Write a Python program to handle a list of 10 numbers. The program will prompt
# the user to handle any of the following operations.
# a) Add a new number to the end of the list.
# b) Remove the first occurrence of a specific number from the list.
# c) Calculate the sum of all the numbers in the list.
# d) Find the min and max value of the list
# e) Sort the list in descending order
# f) Create a sub list based on user input (index or item)

a = []
length = int(input("enter the length of the list : "))
for i in range(0, length):
    b = int(input("enter value : "))
    a.append(b)
print("----menu----"
      "\na. Add a new number to the end of the list."
      "\nb. Remove the first occurrence of a specific number from the list."
      "\nc. Calculate the sum of all the numbers in the list."
      "\nd. Find the min and max value of the list"
      "\ne. Sort the list in descending order"
      "\nf. Create a sub list based on user input (index or item)")
op = (input("enter your option : "))
op.lower()
if op == 'a':
    n = int(input("enter number to add : "))
    a.append(n)
    print("the new list :\n", a)
elif op == 'b':
    n = int(input("enter number to remove : "))
    if n in a:
        a.remove(n)
        print("the element was successfully removed")
        print(a)
    else:
        print("the element not found")
elif op == 'c':
    print("the sum of all elements : ", sum(a))
elif op == 'd':
    print("the maximum value of list : ", max(a))
    print("the minimum value of list : ", min(a))
elif op == 'e':
    a.sort(reverse=True)
    print("the descending order of the list :\n", a)
elif op == 'f':
    n = int(input("enter index to create a sublist : "))
    index = int(n)
    sublist = a[index:]
    print("The sublist is:", sublist)
else:
    print("enter valid option")

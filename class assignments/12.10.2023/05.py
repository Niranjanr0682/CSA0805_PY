# Write a Python program to handle a predefined list with mixture of data (numbers,
# characters). The program will prompt the user to handle any of the following
# operations.
# a) Add a new string to the specific location of the list.
# b) Extend the list with new number
# c) Find the number of occurrence of a specific item in the list
# d) Sort the list in descending order
# e) Replace the item with another new item

n = [10, 'hello', 20, 'python', '@']
print("____Menu____")
print("a. Add a new string to a specific location")
print("b. Extend the list with a new number")
print("c. Find the number of occurrences of a specific item")
print("d. Sort the list in descending order")
print("e. Replace an item with a new item")

op = input("Enter choice: ")

if op == 'a':
    index = int(input("Enter index: "))
    string = input("Enter string: ")
    n.insert(index, string)
elif op == 'b':
    number = int(input("Enter number: "))
    n.append(number)
elif op == 'c':
    item = input("Enter item: ")
    print("Occurrences:", n.count(item))
elif op == 'd':
    n.sort(reverse=True)
    print("List sorted in descending order:", n)
elif op == 'e':
    old_item = input("Enter item to replace: ")
    new_item = input("Enter new item: ")
    for i in range(len(n)):
        if n[i] == old_item:
            n[i] = new_item
    print("List after replacement:", n)
else:
    print("Invalid choice")




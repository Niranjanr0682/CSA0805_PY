# Create a program that defines a function for sorting a list of names.txt in
#     alphabetical order. Allow the user to enter a list of names.txt, and use the sorting
#     function to display the names.txt in sorted order.

def sort_names(names):
    return sorted(names)


num_names = int(input("Enter the number of names.txt: "))
names_list = []

for i in range(num_names):
    name = input(f"Enter name {i + 1}: ")
    names_list.append(name)

sorted_names = sort_names(names_list)
print("Sorted names.txt:")
for name in sorted_names:
    print(name)

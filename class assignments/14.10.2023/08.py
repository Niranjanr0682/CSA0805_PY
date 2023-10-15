# Write a program to prompts user for a new name and appends it to an existing text
# file.

def append_name_to_file(file_name, new_name):
    with open("studentlist.txt", 'a') as file:
        file.write( new_name + '\n')


new_name = input("Enter a new name to append to the file: ")
append_name_to_file('studentlist.txt', new_name)

print("New name has been appended to the file.")

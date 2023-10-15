# Write a program that update the studentlist file, user should be able to specify the
# search and replacement words, the program will search for searches for a specific
# word, and replaces it with another word based on user’s input.

def update_file(file_name, search_word, replace_word):
    updated_content = []
    with open('studentlist.txt', 'r') as file:
        for line in file:
            updated_line = line.replace(search_word, replace_word)
            updated_content.append(updated_line)
    with open('studentlist.txt', 'w') as file:
        file.writelines(updated_content)


search_word = input("Enter the word to search for: ")
replace_word = input("Enter the word to replace it with: ")
update_file('studentlist.txt', search_word, replace_word)

print("File updated successfully.")




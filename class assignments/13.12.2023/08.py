# Read a text file, count the number of occurrences of each word, and print the results.

file = open("C://other stuffs//P for Programming//Github//SIMATS/"
            "/Python project//semester//fruits.txt", "r")
word_count = {}
for line in file:
    line = line.strip()
    words = line.split()
    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
file.close()

for key in list(word_count.keys()):
    print(key, ":", word_count[key])
A
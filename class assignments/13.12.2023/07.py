# Given a dictionary, write a program to print the keys and values in alphabetical order.

dit = {"cherry": 4, "kiwi": 5, "apple": 2, "mango": 1, "banana": 3, }
keys = sorted(dit)
for key in keys:
    value = dit[key]
    print(key, value)

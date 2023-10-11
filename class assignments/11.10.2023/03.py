# Write a program that uses a for loop to print all even numbers from 1 to 20, but skip
# the number 10 in the loop using the continue keyword.
print("the even numbers from 1 to 20 are")
for i in range(1, 21):
    if i % 2 == 0:
        if i == 10:
            continue
        print(i)

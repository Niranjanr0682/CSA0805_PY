# Write a program that uses nested loops to print a pattern of asterisks in the shape of
# a right-angled triangle. Allow the user to specify the number of rows in the triangle.


r = int(input("enter number of rows : "))
for i in range(r+1):
    for j in range(i):
        print("*" , end = "")
    print()

i = int(input("enter rows : "))
a=0
while a<=i:
    j = 0
    while j < a:
        print("*", end="\t")
        j +=1
    print(end="\n")
    a += 1


# Write a program to accept a series of students’ marks from user tills user enter -1.
# The program will perform the following operations;
# a.     Calculate the average marks.
# b.     Find highest and lowest marks.
# c.     Find the number of students failed the module  (below 50 marks)

marks = []
print("enter '-1' to quit.")
try:
    record = int(input("enter marks : "))
    if 0 < record < 101:
        while record != -1:
            marks.append(record)
            record = int(input("enter marks : "))
    else:
        print("invalid input")
    print("____menu____"
          "\na. to calculate the average marks"
          "\nb. to find the highest and lowest mark"
          "\nc. to find the number of students who failed"
          "\nd. to quit")
    operation = input("enter option to proceed : ")
    while operation:
        if operation == 'a':
            s = sum(marks)
            avg = s / len(marks)
            print("the class average mark is : %d" % avg)
            break
        elif operation == 'b':
            print(f"the highest mark of the class is: {max(marks)}")
            print(f"the lowest mark of the class is : {min(marks)}")
            break
        elif operation == 'c':
            failure = 0
            for i in marks:
                if i < 50:
                    failure += 1
            print(f"the number of failed students: {failure}")
            break
        else:
            print("enter valid option")
            operation = input("enter option to proceed : ")
except ValueError:
    print("error message : invalid value entered")

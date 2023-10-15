# Write a program that amend the Q2 and counts the number of student in it. Print
# the student count at the end of the program.

with open('studentlist.txt', 'r+') as file:
    lines = file.readlines()
student_count = 0
for line in lines:
    print(line.strip())
    student_count += 1
print("\nNumber of students:", student_count)



# Write a program that reads the content of file in q1 and display it on the screen.

with open("studentlist.txt", "r") as f:
  contents = f.read()

print(contents)

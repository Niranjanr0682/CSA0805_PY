# Write the following content into a file called studentlist.txt
#         Hari Prasanth
#         Dinesh Raj
#         Magaraju Mohith
#         Teja sri

with open("studentlist.txt", "w") as f:
    f.write("Hari Prasanth\n")
    f.write("Dinesh Raj\n")
    f.write("Magaraju Mohith\n")
    f.write("Teja sri\n")

print("The contents successfully updated")

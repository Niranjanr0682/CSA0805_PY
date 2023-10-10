n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))
print("which operation you need ")
print("add-'a',sub-'s',multiply-'m',divide-'d'")
op = input("enter operation u need to do : ")
op = op.lower()
if op == 'a':
    print("the addition of given number : ", n1 + n2)
elif op == 's':
    print("the subtraction of given number : ", n1 - n2)
elif op == 'm':
    print("the multiplication of given number : ", n1 * n2)
elif op == 'd':
    if n2 != 0:
        print("the division of given number : ", n1 / n2)
    else:
        print("invalid numbers to do division ")
else:
    print("invalid character")
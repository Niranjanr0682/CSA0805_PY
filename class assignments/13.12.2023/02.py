# Write a function to calculate the factorial of a given number.

while True:
    try:
        no = (int(input("enter a number to find the factorial :")))
        if no > 0:
            def fac(x):
                fact = 1
                for i in range(1, x + 1):
                    fact = fact * i
                return fact

            print("\nthe factorial of the given number %d is %d." % (no, fac(no)))
            break
        else:
            print("enter valid integer")
    except ValueError:
        print("enter valid integer")

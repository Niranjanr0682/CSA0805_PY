Year = int(input("enter year to check if it is leap year : "))
if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print("The year", Year, "is 'leap year'")
        else:
            print("The year", Year, "is not 'leap year'")
    else:
        print("The year", Year, "is 'leap year'")
else:
    print("The year", Year, "is not 'leap year'")
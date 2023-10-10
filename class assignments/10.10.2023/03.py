mark = int(input("enter marks : "))
if mark < 0 or mark > 100:
    print("invalid mark")
else:
    if mark >= 85:
        print("A grade")
    elif mark >= 65:
        print("B grade")
    elif mark >= 50:
        print("C grade")
    else:
        print("fail (F)")

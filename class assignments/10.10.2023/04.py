dc = int(input("enter temperature in degree celsius : "))
df = ((dc * 9) / 5) + 32
print("The temperature in celsius    : %d'C " % dc)
print("The temperature in fahrenheit : %.2f'F" % df)
if dc >= 30:
    print("the whether is \"hot\" ")
elif 20 <= dc < 30:
    print("the whether is \"moderate\"")
else:
    print("the whether is \"cold\"")

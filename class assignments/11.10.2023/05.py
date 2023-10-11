# Write a program to find the sum of each even number, given range of values. User
# will determine the range of value by entering the starting value and ending value.
i = int(input("enter initial value : "))
e = int(input("enter stop value : "))
a = i
s = 0
while i <= e:
    if i % 2 == 0:
        s += i
    i += 1
print("the sum of even numbers from %d to %d is %d" % (a, e, s))

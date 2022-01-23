# Question 1
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=",")


# Question 2
fname = input("Enter firstname ")
lname = input("Enter lastname ")
print(lname + " " + fname)


# Question 3
diameter = 12
r = diameter / 2
volume = (4/3) * 3.14 * (r ** 3)
print(volume,"cm^3")
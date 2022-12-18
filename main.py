issearch = False
index = 0
number = [22, 7, 3, 44, 90, 87, 69]
numbers = int(input("Enter any numbers to get arranged : "))
for i in (number):
    if (numbers == i):
        issearch = True
        break
    else:
        index = index+1
if (issearch == True):
    print("Number is found at ", index+1, " position")
else:
    print("Numbers is not found")
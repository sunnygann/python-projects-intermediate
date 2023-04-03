listA = input("Please input a list of numbers delimited by ' ': ")
listB = input("Please input another list of numbers delimited by ' ': ")
intV = input("Please enter a number: ")

aList = listA.split()
bList = listB.split()
sumTwo = False

for x in aList:
    for y in bList:
        if (int(x) + int(y)) == int(intV):
            sumTwo = True

print(sumTwo)
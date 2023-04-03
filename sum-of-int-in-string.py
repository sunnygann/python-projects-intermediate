userString = input("Enter anything: ")

stringList = userString.split()
sumInts = 0
countInts = 0

for word in stringList:
    try:
        if int(word):
            countInts += 1
        sumInts += int(word)
    except ValueError:
        continue

print("There are " + str(countInts) + " integers.")
print(sumInts)
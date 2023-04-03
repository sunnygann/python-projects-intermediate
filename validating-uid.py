uidList = []

testCases = input()

for i in range(int(testCases)):
    uidList.append(input())

for x in uidList:
    if x.isalnum():
        charCheck = ''
        digitCount = 0
        upperAlphaCount = 0
        breakStatus = False
        if len(x) == 10:
            for i in x:
                if i.lower() in charCheck:
                    print("Invalid")
                    breakStatus = True
                    break
                charCheck += i.lower()
                if i.isalpha():
                    if i.isupper():
                        upperAlphaCount += 1
                if i.isdigit():
                    digitCount += 1
            if upperAlphaCount >= 2 and digitCount >= 3 and breakStatus == False:
                print("Valid")
            elif breakStatus == False:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
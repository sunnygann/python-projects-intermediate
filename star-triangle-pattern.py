''' numChars = userInput * 2
    numSpace = userInput * 2 - (lineNum * 2 - 1)
    numStars = userInput * 2 - numSpace '''

try:
    userInput = int(input("Please enter a valid integer value: "))

    numChars = userInput * 2

    for i in range(userInput):
        string = ''
        stringList = []
        numSpace = userInput * 2 - ((i + 1) * 2 - 1)
        numStars = userInput * 2 - numSpace

        for x in range(numChars):
            if numSpace >= (x + 1):
                stringList.append(' ')
            else:
                stringList.append('*')

        for char in stringList:
            string += char

        print(string)

except ValueError:
    print("Please enter a valid integer value")

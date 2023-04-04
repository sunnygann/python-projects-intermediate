stuGrades = []
nameList = []

N = int(input())

if N < 2 or N > 5:
    exit
else:
    for x in range(N):
        stuGrades = []
        stuGrades.append(input())
        try:
            stuGrades.append(float(input()))
        except ValueError:
            print("Please enter a valid number.")
        nameList.append(stuGrades)

    gradesList = []
    for x in range(len(nameList)):
        gradesList.append(nameList[x][1])
    gradesList = sorted(gradesList, reverse = True)

    for i in range(len(gradesList)):
        if not gradesList[len(gradesList) - (i+1) ] == gradesList[len(gradesList) - (i+2)]:
            secondLowest = gradesList[len(gradesList) - (i+2)]
            break
    secondLowestNames = []
    for x in nameList:
        if x[1] == secondLowest:
            secondLowestNames.append(x[0])
    secondLowestNames = sorted(secondLowestNames)

    for x in secondLowestNames:
        print(x)
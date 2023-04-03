userString = input("Enter anything: ")

num = ''

for i in userString:
    if i.isdigit():
        num += i
    else:
        num += ' '

numList = num.split()
sum = 0

for x in numList:
    sum += int(x)

print(sum)
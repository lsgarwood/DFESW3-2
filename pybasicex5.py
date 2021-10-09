#Exercise 5: Check if the first and last number of a list is the same
#Given list: [10, 20, 30, 40, 10]
#result is True
#numbers_y = [75, 65, 35, 75, 30]
#result is False


#Answer1
#numbers_x = [10,20,30,40,10]
#numbers_y = [75,65,35,75,30]
#numbers_z = [8,43,72,6,8]

#input = numbers_z
#print(input)

#if input[0] == input[4]:
#    print(True)
#else:
#    print(False)

#Answer2
inputNums = input('Please enter 5 numbers seprated by spaces:')
numList = inputNums.split()

for i in range(len(numList)):
        numList[i] = int(numList[i])

firstnum = numList[0]
lastnum = numList[4]

def result(numList):
    if firstnum == lastnum:
        return True
    else:
        return False

print('Given list: ', numList)
print('Do the first and last numers match?')
print('Result:', result(numList))
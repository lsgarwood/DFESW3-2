
def sum(numList):
    total = 0
    for x in numList:
        total += x
    return total

numbers = input('Please enter a list of numbers separated by spaces:')
numList = numbers.split()
for i in range(len(numList)):
    numList[i] = int(numList[i])
total = sum(numList)
print('Total of these numbers is: ', total)

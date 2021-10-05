def maxNum(numList):
    max = numList[0]
    for x in numList:
        if x > max:
            max = x
    return max

nums3 = input('Please enter three numbers separated by spaces:')
numList = nums3.split()
for i in range(len(numList)):
    numList[i] = int(numList[i])

print("Largest number is: ", (maxNum(numList)))
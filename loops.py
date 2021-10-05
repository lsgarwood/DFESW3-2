#for i in range(5, 11):
#    print(i)

#count = 0
#name = str(input("What is your name?"))
#newname = input('Give me another name:')

#while count < 5:
#    print(name, "is awesome!")
#    count += 1
#    name = newname

#names = 0
#name = input('please enter name')

#while names < 5:
#    print(name, 'is awesome!')
#    names = names + 1 

#var = []

#for i in range(1500, 2701):
#    if (i%7 and i%5):
#        var.append(str(i))
#print (','.join(var))


#inputNamesList = []
#numVar = 5
#while numVar > 0:
#    inputNameVar = input('Type IN: ')
#    inputNamesList.append(inputNameVar)
#    numVar = numVar - 1

#varName = input("Please enter a name to check if it's a palindrome: ").lower()

#varCheck = ''

#for i in range(len(varName)-1,-1,-1):

#    varCheck = varCheck + varName[i]

#if varCheck == varName:

#    print("Congrats your name is a palindrome: " + varName)

#else:

#    print("Sorry: " + varName + " Is not a palindrome")

#palinVar = input('TYPE IN: ')
#numChars = len(palinVar) - 1
#raVnilap = ''
#while numChars >= 0:
#    raVnilap = raVnilap  + palinVar[numChars]
#    numChars = numChars - 1
#if raVnilap == palinVar:
#    print('PALINDROME')
#else:
#    print('no')

#testVar = input('TEMPIN: ')
#lastIndex = len(testVar) - 1
#print(testVar[lastIndex])
#print(testVar[0:(lastIndex)])

#if varNum == 7:
#    print('YOU WIN!')
#elif varNum < 7:
#    print('You guessed too low')
#elif varNum > 7:
#    print('You guessed too high')

#while guess == 7:
#    print('YOU WIN!')
#    if guess > 7:
#        print('You guessed too high')
#    elif guess < 7:
#        print('You guessed too low')

#import random
#exitchoice = 'nothing'
#while exitchoice != 'EXIT':
#    number = int(input('Enter a number between 0-9: '))
#    if number == random.randint(1,10):
#        print('YOU WIN!')
#    else:
#        print("Sorry, you didn't enter correctly!")
#        print('TRY AGAIN!')
#    exitchoice = input("Press return to play again, or type EXIT to leave.")

#for x in range(6):
#    if(x == 3 or x == 6):
#        continue
#    print(x, end=' ')
#print('\n')

word = input('Input a word to reverse: ')

for rev in range(len(word)-1, -1, -1):
    print(word[rev], end=' ')
print('\n')

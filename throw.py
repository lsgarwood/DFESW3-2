import dice

playerInput = str(input('Press Enter to roll the dice!'))
throw1 = dice.roll()
throw2 = dice.roll()
if playerInput == 'Enter':
    print(f'You got: {throw1, throw2}')

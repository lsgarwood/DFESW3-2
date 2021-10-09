#exercise 1 Calculate the multiplication and sum of two numbers
#1                  #2
# number1 = 20      # number1 = 40
# number2 = 30      # number2 = 30
# output = 600      # output = 70

# return product(*) if > 1000, else return sum(+) 

number1 = int(input('Enter a number:'))
number2 = int(input('Enter another number:'))

def productcalc(number1, number2):
    product = (number1 * number2)
    
    if product < 1000:   
        return product
    else:
        return (number1 + number2)

outputVar = productcalc(number1, number2)
print('The output is:', outputVar)
#Exercise 3: Print characters from a string that are present at an even index number

#expected output
#Orginal String is  pynative
#Printing only even index chars
#p
#n
#t
#v

inputstring = str(input('Please enter a word or string of characters:'))
print('Original string is:' + inputstring)
print('Printing only even index characters...')

for i in range(0, len(inputstring), 2):
    output = inputstring[i] 
    print(output)


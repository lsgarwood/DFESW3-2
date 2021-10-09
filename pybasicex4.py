#Exercise 4: Remove first n characters from a string

#For example:
#remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
#remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
#Note: n must be less than the length of the string.

stringVar = str(input('Please enter a word or string of characters:'))
numberVar = int(input('Enter number of characters to remove from start of string:'))
i = numberVar

if numberVar < len(stringVar):
    print(stringVar[i: ])
else:
    toobigVar = int(input('Sorry, this number has to be less that the number of characters you entered:'))
    i = toobigVar
    if toobigVar < len(stringVar):
        print(stringVar[i: ])
        
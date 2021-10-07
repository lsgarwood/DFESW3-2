
class Letters():
    
    def __init__(self,lettercheck):
        self.lettercheck = lettercheck

    def checkstring(self,x):
        return x in self.lettercheck

vowelchecker = Letters('AEIOU')
letterwithoneendpoint = Letters('P')
lettersnoenclosedareas = Letters('CEFGIJKLMNSTUVWXYZ')
dottedinlowercase = Letters('IJ')

print(vowelchecker.checkstring('A'))
print(vowelchecker.checkstring('P'))
print(letterwithoneendpoint.checkstring('L'))
print(letterwithoneendpoint.checkstring('H'))
print(lettersnoenclosedareas.checkstring('D'))
print(dottedinlowercase.checkstring('I'))
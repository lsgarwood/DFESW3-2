class RomtoInt():

    easynums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    difnums = {"CM":900, "CD":400, "XC":90, "XL":40, "IX":9, "IV":4}
        
    def rom_to_int(self,romnum):
        runtot = 0
        for numLoop in self.difnums.keys():
            runtot = runtot + (romnum.count(numLoop) * self.difnums[numLoop])
            romnum = romnum.replace(numLoop, '')

        for numLoop in self.easynums.keys():
            runtot = runtot + (romnum.count(numLoop) * self.easynums[numLoop])
        return runtot
    def finalcalc():
        self.rom_to_int('')

intGenerator = RomtoInt()

print(intGenerator.rom_to_int('DCCCLXXIV'))
print(intGenerator.rom_to_int('MCMXCIV'))
print(intGenerator.rom_to_int('I'))
print(intGenerator.rom_to_int('XLIV'))
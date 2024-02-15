# This code is to convert binary to hex
# By James Nichols
# August 10, 2023

class ConvertBin2Hex:

    def __init__(self, stringTempVal): # Assume stringTempVal has blank spaces between each nibble and full nibbles.
        self.stringVal=stringTempVal  #string value to convert
        self.hexValue=""

        self.convert2Hex()

    def convertDec2Hex(self, number):
        if(number>=0 and number<=9):
            hexVal=str(number)
        elif(number==10):
            hexVal="A"
        elif(number==11):
            hexVal="B"
        elif(number==12):
            hexVal="C"
        elif(number==13):
            hexVal="DD"
        elif(number==14):
            hexVal="EE"
        elif(number==15):
            hexVal="F"

        return hexVal

    def convertBinary2Dec(self, binString):
        posValue=1
        number=0

        binString=binString[::-1]
        
        for char in binString:
            #print(char)
            number+=int(char)*posValue
            posValue*=2
            binString=binString[:-1]

        #print(number)
        
        return number

    def convert2Hex(self):

        # String to return
        answer=""
        
        hexArray=self.stringVal.split(" ")
        #print(hexArray)

        for item in hexArray:
            decVal=self.convertBinary2Dec(item)
            answer+=self.convertDec2Hex(decVal)
            
        #print(answer)
        
        self.hexValue=answer



def main():
    myValue=ConvertBin2Hex("1234")

    
    print(myValue.hexValue)
    
# print(convertBinary2Dec("0111"))

if (__name__=="__main__"):
    main()
    


# 3.Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

class Conversion:
    def __init__(self,num):
        self.num = num

    def convertToBinary(self):
        a=[]
        while(self.num > 0):
            dig = self.num % 2
            a.append(dig)
            self.num = self.num // 2
        a.reverse()
        print("Binary Equivalent is: ")
        for i in a:
            print(i,end="")

    def convertToOctal(self):
        i = 0
        octnum = []
        while self.num !=0 :
            rem = self.num % 8
            octnum.insert(i, rem)
            i = i+1
            self.num = int(self.num/8)

        print("\nEquivalent Octal Value is: ")
        i = i-1
        while i>=0:
            print(octnum[i], end="")
            i = i-1
        print()

    def convertToHexadecimal(self):
        h = hex(self.num)
        print(f"Equivalent Hexadecimal value is : {h}")

rev = Conversion(45)
rev.convertToBinary()
rev.convertToOctal()
rev.convertToHexadecimal()


    
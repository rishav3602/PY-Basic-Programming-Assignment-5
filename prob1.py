# 1.Write a Python Program to Find LCM?



num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
    
if num1 > num2:
    great = num1
else :
    great = num2
    
while True :
    if (great%num1==0) and (great%num2==0):
        LCM = great
        break
    great += 1
    

print(f"The L.C.M. of {num1} and {num2} is : {LCM}")




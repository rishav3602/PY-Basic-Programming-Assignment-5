# 2.Write a Python Program to Find HCF?

num1 = int(input("Enter your first number : "))
num2 = int(input("Enter your second number : "))
 
if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range (1,smaller+1):
    if (num1%i==0) and (num2%i==0):
        hcf = i
        
print(f"The H.C.F. of {num1} and {num2} is : {hcf} ")

# 5.Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

class Calculator:
    def add (x,y):
        return x + y

    def sub (x,y):
        return x - y

    def mul (x,y):
        return x * y

    def div (x,y):
        return x / y

    while True:

        num1 = float(input("Enter your first number : "))
        num2 = float(input("Enter your second numbe : "))
        opr = input("Select the operator : add(+) , subtract(-) , multiply(*) , divide(/) : ")

        if opr == "+":
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif opr == "-":
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        elif opr == "*":
            print(f"{num1} X {num2} = {mul(num1,num2)}")
        elif opr == "/":
            print(f"{num1} / {num2} = {div(num1,num2)}")
        else :
            print("invalid input")
        
        next_calculation = input("Select YES(y) or NO(n) to do next calculation: ")
        if next_calculation == "n":
            break
        elif next_calculation == "y":
            continue
        else:
            print("invalid input")
            break

num = Calculator()
# 4. Write a Python Program To Find ASCII value of a character?


class ASCII:
    def __init__(self):
        self.c = input("Enter your character : ")
        print("The ASCII value of '" + self.c + "' is", ord(self.c))

obj = ASCII()
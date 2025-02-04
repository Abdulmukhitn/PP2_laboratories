import math

class MyString:
    def getString(self):
        self.s = input("Enter a string: ")
    def printString(self):
        print(self.s.upper())

s = MyString()
s.getString()
s.printString()



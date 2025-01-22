print("Hello, World!")


import sys

print(sys.version)


if 5 > 2:
  print("Five is greater than two!")


if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 



x = 5
y = "Hello, World!"


#This is a comment.
print("Hello, World!")


#This is a comment
#written in
#more than just one line
print("Hello, World!")



"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


x = 5
y = "John"
print(x)
print(y)




x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)



x = "John"
# is the same as
x = 'John'


a = 4
A = "Sally"
#A will not overwrite a


#multiple  variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)



x = "Python "
y = "is "
z = "awesome"
print(x + y + z)



x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#global variables

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


#data types
x = "Hello World"
x = 20	
x = 20.5	
x = 1j
x = ["apple", "banana", "cherry"]	
x = ("apple", "banana", "cherry")	
x = range(6)
x = {"name" : "John", "age" : 36}	
x = {"apple", "banana", "cherry"}	
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"	
x = bytearray(5)		
x = memoryview(bytes(5))	
x = None



print(type(x))
print(type(y))
print(type(z))


#random
import random

print(random.randrange(1, 10))


#strings
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')




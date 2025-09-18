#Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

print()
#Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print()

x = y = z = "Apple"
print(x)
print(y)
print(z)

print()

#Output Variables
a=5
d=4
print(a+d)

print()
'''in the print() function, you output multiple variables, separated by a comma and 
use the + operator to output multiple variables '''

s="shonqan"
l='likes'
b='banana'
print(s,l,b)
print(b+" "+l+" "+s)

print()

#Global Variables
# a variable outside of a function, and using it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print()

#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print()
#global keyword, the variable belongs to the global scope
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print()

#use the global keyword if you want to change a global variable inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

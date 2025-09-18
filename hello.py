#Getting Started
print("Hello, World!")

print()
#Syntax1
if 5 > 2:
  print("Five is greater than two!")
print()  
#Syntax2
if 6 > 2:
 print("six is greater than two!") 
if 6 < 2:
        print("six is less than two!") 
 
print()       
#Creating Variables
x = str(3)    
y = int(3)    
z = float(3)
y = "zhansaya"
print(x)
print(y)
print(z)
print(type(x))
print(type(y))

print()
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

s="shonqan"
l='likes'
b='banana'
print(s,l,b)
print(b+" "+l+" "+s)

print()

#Global Variables
x = "awesome"

print()

def myfunc():
  print("Python is " + x)

myfunc()

print()

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print()

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Python Numbers
x = 1    
y = 2.8  
z = 1j   
print(type(x))
print(type(y))
print(type(z))

print()

#Type Conversion
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

print()

#Random Number
import random

print(random.randrange(1, 15))

print()
#Python Casting

"""int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals """

x = int(1)   
y = int(2.8) #округляет
z = int("3") 
print(x,y,z)
print(type(x))
print()

x = float(1)     
y = float(2.8)  
z = float("3")  
w = float("4.2") 
print(x,y,z,w)
print(type(x))
print()

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)
print(type(x))

print()
#Quotes Inside Quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


print()

#Strings are Arrays

a = "Hello, World!"
print(a[0])


print()
print()
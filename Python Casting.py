
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
#1
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
#Looping Through a String
for x in "banana":
  print(x)

print() 

#len() function
print(len(a))

print()

#2
#Slicing
b = "Hello, World!"
print(b[2:5])

print(b[-5:-2])

#3
#Modify
a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))

#4
#String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b
print(c)
#5
#String Format
txt = f"The price is {20 * 59} dollars"
print(txt)

#6 Escape Characters
#To fix this problem, use the escape character \"


#Chapter 2.2 - Variables Continued

#In python3, a variable name can be a short descriptive name, but should follow some rules

#Rule:
#Legal variable name
"""
myvar = "Hello World"
_my_var = "Hello World"
my_var = "Hello World"
myVar = "Hello World"
MYVAR = "Hello World"
myVar2 = "Hello World"

#Illegal variable name
2myvar = "Hello World"
my-var = "Hello World"
my var = "Hello World"
"""

#Now lets learn assigning multiple values to multiple Variables

#Example 

x, y, z = "John", "Rupert", "James"
print(x)
print(y)
print(z)

#You can also assign one value to multiple Variables
#Example

x = y = z = "John"

print(x)
print(y)
print(z)


#you can also unpack values from list
#Example 

names = ["John", "Rupert", "James"]
x, y, z = names
print(x)
print(y)
print(z)


#Pythons allows to print multiple variable in a single print statement using , or if all the variables are string, then you can also use +
#Example
x = "Hello"
y = "World"

print(x, y)
print(x + y)



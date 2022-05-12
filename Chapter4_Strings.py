#Chapter 4 - Strings
#in python you can assign string using "" or ''

#Example

a = 'hello world'
b = "Hello World"

print(a, b)

#You can also use """ or ''' for Strings
#Example



b = '''Hello my name is Andy'''

print(a)
print(b)


#Now let's try and SLICE a string

#Example

a = "Hello World"

print(a[2:4])

#first number is for starting index and second number is for ending index

#let's try something with SLICING of string

a = "Hello my name is James"
print(a[:5])

#When you don't assign starting index, it is by default taken as 0
#same goes for ending index

print(a[5:])


#Now we will learn some pre defined functions for string
#first, lets try to uppercase our string
#to achieve this, we will use upper() functions
#Example 

a = "hello world"
print(a.upper())


#You can do the same for lower case

#Example 

a = "HELLO WOrld"
print(a.lower())


#now let's try to remove whitespace

a = " hello world "
print(a.strip())


#You can replace string using replacxe function
#Example

a = "Hello World"

print(a.replace("H", "R"))


#You can split string using .split()
#Example

a = "Hello World"

print(a.split("W"))

#the letter W has been removed and the string has been split into two

#Now, let's concatinate two string

a = "hello"

b = "world"


print(a+b)

#but when you want to add another string such as a white space, you will use

print(a+" "+b)

# now lets learn about formatting of String

#Example 

a = "hello"
b = 6

c = a + b

print(c)

#as you can see, we are getting an error.
#to fix this, we'll be using formatting


a = 6
b = "Hi nmy age is {}"

print(b.format(a))

#you can assign your different data type variable anywhere using {} and .format()

#lets say you have multiple variables that need to assigned in an order

#Example

a = 6
b = 7
c = 9
d = "Hello {}, world {}, Cat{}"

print(d.format(a,b,c))


#Now, let's say you want return the index of any certain world#you can use .count()
#Example

a = "Hello my name johnny"
print(a.count("my"))

#as you can see, the index of "my" is 1, when you count from 0.

#You can capitilize all starting letters of your sentence or string using .title()

#Example
a = "hello my name is jordan"

print(a.title())
# Introducing Python Basics

## Topics:

* Print() Function
* Whitespace
* Python Trace-back error reporting
* Variables
* Introducing Data Types
* Specify a Variable Type - Python Casting
* Basic Calculation Operands
* String Concatenation
* The Print Function Syntax


### Code Examples
---
```python
# ex1.0.1 Print to terminal
print("hello world")
```
```python
# ex1.0.2 Whitespace
# Spaces, Tabs, and End-of-line symbols
print(" hello world ")
```
```python
# ex1.0.3 Python Traceback error report
print(hello world") # Error on this line
# Output:   
#     File "C:\example.py", line 1
#     print(hello world")
#                 ^
# SyntaxError: invalid syntax
```
```python
# ex1.0.4 Python comments
# This is a single line comment

# This is a 
# multiline comment
```
```python
# ex1.0.5 Printing a Variable - String (str)
x = "hello world"
print(x)
```
```python
# ex1.0.6 Printing a Variable - Error Traceback
x = "hello world"
print(y)
# Output:
#   Traceback (most recent call last):
#   File "C:\example.py", line 2, in <module>
#   print(y)
# NameError: name 'y' is not defined
```
```python
# ex1.0.7 Printing a Variable - Integer (int)
x = 1
print(x)
```
```python
# ex1.0.8 Printing a Variable - functions to manipulate strings
x = "hello world"
print(x.title())
print(x.upper())
print(x.lower())
# Output: Hello World HELLO WORLD hello world
```
### Data Types

We focus on str, int and float initially. If you get time, familiarize yourself with the other data types

---
* Text Type:	str
* Numeric Types:	int, float, complex
* Sequence Types:	tuple, list, range
* Mapping Type:	dict
* Set Types:	set, frozenset
* Boolean Type:	bool
* Binary Types:	bytes, bytearray, memoryview
---

```python
# ex1.0.9 Example printing different data types
x = "String" # String
y = 2 # Integer
z = 3.1 # Float
print(x, y, z)
```
```Python
# ex1.1.0 Casting data types
# Python is strongly and a dynamically typed language
x = str("String") # String
y = int(2) # Integer
z = float(3.1) # Float
print(x, y, z)
```
```Python
# ex1.1.1 Identifying the data type
x = str("String") # String
print(type(x))
# Output <class 'str'>
```
```python
#  
x = "hello"
y = "world"
print(x,y)
```
```python
# ex1.1.3 Python string concatenation
x = "hello"
y = "world"
print(x + y)
```
```python
#ex1.1.4 Using basic math operators
x = 1
y = 2
# First Python evaluate the expression on the right
z = 1 + 1
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(z)
```

### Data Types

Python Arithmetic operators to perform common mathematical operations:

---
* \+	Addition	x + y	
* \-	Subtraction	x - y	
* /	Division	x / y	
* \*	Multiplication	x * y	
* %	Modulus	x % y	
* **	Exponentiation	x ** y	
* //	Floor division 	x // y
---

```python
# ex1.1.5 String multiplication
x = "hello"
y = "world"
print((x + y)*5)
# Output helloworldhelloworldhelloworldhelloworldhelloworld
print((x , y)*5)
# Output: ('hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world')
```
```python
# ex1.1.6 Printing multiple data types with concatenation 
x = "zander"
y = 1
print(x + str(y))
print(x + " is " + str(y))
```
```python
# ex1.1.7 Printing multiple data types continued
x = "1"
y = 1
print(int(x) + y)
```
```python
# ex1.1.8 New line character
print("x") # Behind the scenes \n is used to create
print("y") # a new line
print("zander\npark") # Creates a new line after zander
```
```python
# ex1.1.9 New line character with variables and concatenation
x = "first name: zander"
y = "surname: park"
print(x + "\n" + y)
```
```python
#  
# print(object(s), sep=separator, end=end, file=file, flush=flush)
x = "a"
y = "b"
z = "c"
print(x, y, z, sep='\n')
print(x, y, z, sep=',+')
# Output: a,+b,+c
print(x, y, z, end=' ++++')
# Output: a b c ++++
```

## 001 Code Challenges

Use the previous code examples to help you complete the code challenges:
### **Challenge 1-7**
1. Get comfortable with your environment. Output hello world (if on Windows) using the command prompt start > CMD, the Python IDLE and in the Visual studio code editor terminal.
2. Create 2 new variables, name and surname. Print the variables so that they appear of individual lines and so that the first letter is capitalized.
3. Create a third variable, age. Print the age to appear below the surname.
4. Create name, surname and age variables for a new person.
5. Calculate the total age of person 1 + person 2 and print the calculated value.
6. Print out multiple variables separated by a comma (,) defined by the sep parameter (demonstrated in ex1.1.16) on one line.
7. Create a new variable and store a string. Print the variable so that it outputs 5 times, each time on a new line.

---

### **Troubleshooting challenges**
Troubleshoot and fix the following code examples:

```python
# Troubleshooting Challenge 1
print(Hello + World)
```
```python
# Troubleshooting Challenge 2
x = "zander"
y = 1
print(x + y)
print(x + " is " + str(y))
```
```Python
# Troubleshooting Challenge 3
x = "first name: zander"
y = "surname: park"
print(x + "\n" + Y)
```

### Solutions
---
```python
# Challenge 1 Solution
print("Hello World")
```
```python
# Challenge 2 Solution
name = "Zander"
surname = "Park"
print(name.title(), "\n" + surname.title())
```
```python
# Challenge 3 Solution
name = "Zander"
surname = "Park"
age = "20"
print(name, "\n" + surname, "\n" + age)
```
```Python
# Challenge 4-5 Solution
name1 = "Zander"
surname1 = "Park"
age1 = 20
name2 = "Xander"
surname2 = "Park"
age2 = 20
total_age = age1 + age2
print(name1, "\n" + surname1, "\n" + str(age1))
print(name2, "\n" + surname2, "\n" + str(age2))
print("Total age =", str(total_age))
```
```Python
# Challenge 6 Solution
x = 1
y = 2
z = 3
print(x,y,z, sep=",")
```
```python
# Challenge 7 Solution
x = "a"
print((x+"\n")*5)
```
```python
# Solution - Troubleshooting Challenge 1
print("Hello World")
```
```python
# Solution - Troubleshooting Challenge 2
x = "zander"
y = 1
print(x + str(y))
print(x + " is " + str(y))
```
```python
# Solution - Troubleshooting Challenge 3
x = "first name: zander"
y = "surname: park"
print(x + "\n" + y)
```
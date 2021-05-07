# Introducing Python Basics

## Topics:

* Print() Function
* Variables
* Introducing Data Types
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
# ex1.0.2 Python comments
# This is a single line comment

# This is a 
# multiline comment
```
```python
# ex1.0.3 Printing a Variable - String (str)
x = "hello world"
print(x)
```
```python
# ex1.0.4 Printing a Variable - Integer (int)
x = 1
print(x)
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
# ex1.0.5 Example printing different data types
x = "String" # String
y = 2 # Integer
z = 3.1 # Float
print(x, y, z)
```
```Python
# ex1.0.6 Casting data types
# Python is strongly and a dynamically typed language
x = str("String") # String
y = int(2) # Integer
z = float(3.1) # Float
print(x, y, z)
```
```Python
# ex1.0.7 Identifying the data type
x = str("String") # String
print(type(x))
# Output <class 'str'>
```
```python
# ex1.0.8 Python comma in print function
x = "hello"
y = "world"
print(x,y)
```
```python
# ex1.0.9 Python string concatenation
x = "hello"
y = "world"
print(x + y)
```
```python
#ex1.0.10 Using basic math operators
x = 1
y = 2
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
# ex1.0.11 String multiplication
x = "hello"
y = "world"
print((x + y)*5)
# Output helloworldhelloworldhelloworldhelloworldhelloworld
print((x , y)*5)
# Output: ('hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world', 'hello', 'world')
```
```python
# ex1.0.12 Printing multiple data types
x = "zander"
y = 1
print(x + str(y))
```
```python
# ex1.1.013 Printing multiple data types continued
x = "1"
y = 1
print(int(x) + y)
```
```python
# ex1.1.14 New line character
print("x") # Behind the scenes \n is used to create
print("y") # a new line
print("zander\npark") # Creates a new line after zander
```
```python
# ex1.1.15 New line character with variables and concatenation
x = "first name: zander"
y = "surname: park"
print(x + "\n" + y)
```
```python
# ex1.1.16 The print function syntax
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
2. Create 2 new variables, name and surname. Print the variables so that they appear of individual lines.
3. Create a third variable, age. Print the age to appear below the surname
4. Create name, surname and age variables for a new person.
5. Calculate the total age of person 1 + person 2 and print the calculated value
6. Print multiple variables separated by a comma (,) defined by the sep parameter (demonstrated in ex1.1.16)
7. Create a new variable and store a string. Print the variable so that it outputs 5 times, each time on a new line.

### Solutions
---
```python
# Challenge 7 Solution
x = "a"
print((x+"\n")*5)
```
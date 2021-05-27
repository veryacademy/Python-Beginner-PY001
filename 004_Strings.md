# Python Strings

## Topics:
*  New Lines
*  Escape Characters
*  Multiline String
*  Character Positions
*  Character Slicing
*  String Length
*  Modifying Strings
*  String Strip
*  String Replace
*  String Find
*  Count Substring
*  String Formatting

### Code Examples
---

```python
#ex4.0.1 New line
text = "I am 10 \nyears old today"
print(text)
```
```python
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace
```
```python
#ex4.0.2 Python escape character Example 1
print("This is a string")
print("This is a \"string\"")
print('This is a \'string\'')
print("What about \\")
```
```python
#ex4.0.3 Escape Character Example 2
x = "Hello \bWorld!"
print(x) 
x = "Hello \tWorld!"
print(x) 
```
```python
#ex4.0.4 Multiline String
text = """I am 10 
years old today"""
print(text)
```
```python
#ex4.0.5 Get the character at a position
x = "Hello"
print(x[1])
```
```python
#ex4.0.6 Slice a sting
# Slice from start
x = "Hello"
print(b[:4])

# Slice within
x = "Hello"
print(x[1:4])

# Slice End
x = "Hello"
print(x[2:])
```
```python
#ex4.0.6 Return length of string ex1
text = "I am 10 years old today"
print(len(text))
```
```python
#ex4.0.7 Return length of string ex2
text = len("I am 10 years old today")
print(text)
```
```python
#ex4.0.8 Modifying Strings 
text = "hello am 10 years old today"
print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.title())
```
```python
#ex4.0.9 String strip
text = " Hello, I am 10 years old today "
print(text.strip(" "))
```
```python
#ex4.1.0 String Replace
x = "Hello, I am 10 years old today"
print(x.replace("10", "12"))
```
```python
#ex4.1.1 find items in a string
x = "Hello Zander"
y.find("Zander")
print(y)
# Returns 6
# This is the lowest index in the string where the substring is found
```
```python
#ex4.1.2 returns -1 since the substring is not found
x= "Hello Zander"
y = x.find("Zanders")
print(y)
```
```python
#ex4.1.3 string.find(substring, start, end)
x= "Hello Zander"
y = x.find("Zander", 6, 12)
print(y)
```
```python
#ex4.1.4 Using find with a conditional statement
x= "Hello Zander"
y = x.find("Zander")

if y >= 0:
  print("Match found")
else:
  print("Match not found")
```
```python
#ex4.1.5 find() is limited to strings 
x= ["a","b"]
y = x.find("a")
print(y)
```
```python
#ex4.1.6 index() example
# Syntax: string.index(substring, start, end) 
x= ["a","b","c"]
y = x.index("c")
print(y)
```
```python
#ex4.1.7 index() raise an error (ValueError)
x= ["a","b","c"]
y = x.index("d")
print(y)
```
```python
#ex4.1.8 Capture error
x= ["a","b","c"]
try:
    y.index("d")
except ValueError:
      print("Not found")
```
```python
#ex4.1.9 Count substring
x = "How may apples are there is an apple cart?"
y = x.count("apple")
print(y)
```
```Python
#ex4.2.0 The String Modulo Operator
print('Hello, my name is %s.' % 'Zander')
print('Get %d%% off on %s today only!' % (30, 'bananas'))
```
```Python
#ex4.2.1 The String .format() Method: Arguments
print('{} {} cost ${}'.format(6,'bananas',1.74))
```
```Python
#ex4.2.2 Using keyword arguments
print('{quantity} {item} cost ${price}'.format(quantity=6,item='bananas',price=1.74))
```
```Python
#ex4.2.3 F format
x = "a"
print(f"Hey {x}")
```


## 004 Code Challenges
---
Use the previous code examples to help you complete the code challenges

### **Task 1-4**
1. Ask the user to input their username and password twice. If the password is less than 8 characters or does not match, ask the user to re-enter their username and passwords.
2. Sometimes when a user logs in they are provided part of a telephone number for example ***122 to confirm where the security message will be sent. Create an application that first asked the user to enter a telephone number. Replace all but the last 3 numbers in the telephone number with the * character and print the newly formatted number to the terminal
3. Ask the user to type in their first name and surname. Print the users initials (the first letter of their first and surname) to the terminal.
4. Use the list shown below to count the number of instances the number 10 occurs. Calculate the combined total.
```Python
x = [10,1,12,42,51,1010,124,10,23,10,42,52,3,10]
```
5. Use the provided text to help format the text so that a space appears in the text after each full stop.
```
A Free Python Beginners Course for 2021.This is a 10 part course slowly and progressively developing your skills through explanations, examples and code challenges.In this first module we focus on learning the basic underpinning skills used throughout this course, Print, Variables & Data Types.
```
6. Ask the user to type in their name. If their name matches a name is the provided list let the user know. If their name does not match any names in the list capture the ValueError and print a suitable message.
```Python
x = ["Aarav","Zander","Kjetil"]
```

### Solutions
---

```python
# Challenge 1 Solution
x = input("Enter your name: ")
y = input("Enter your password: ")
z = input("Enter your password again: ")

if y == z:
  if len(y) < 8 or len(z) < 8:
    print("Passwords much be at least 8 characters long")
  else:
    print("Thank you your account has been made")
else:
  print("Passwords do not match - please try again")
```
```python
# Challenge 2 Solution
x = input("Enter your phone number:")
y = len(x) - 3
z = x[-3:]
print(("*")*y + z)
```
```python
# Challenge 3 Solution
x = input("Enter your first name: ")
y = input("Enter your surname: ")

x = x[:1]
y = y[:1]
print((x+y).upper())
```
```python
# Challenge 4 Solution
x = [10,1,12,42,51,1010,124,10,23,10,42,52,3,10]
y = x.count(10) * 10
print(y)
```
```python
# Challenge 5 Solution
x = "A Free Python Beginners Course for 2021.This is a 10 part course slowly and progressively developing your skills through explanations, examples and code challenges.In this first module we focus on learning the basic underpinning skills used throughout this course, Print, Variables & Data Types."

y = x.replace(".", ". ")

print(y)
```
```python
# Challenge 6 Solution
x = ["Aarav","Zander","Kjetil"]
y = input("Please enter your name: ")

try:
  x.index(y)
except ValueError:
  print("No match was found")
else:
  print("We have found a name match")
```
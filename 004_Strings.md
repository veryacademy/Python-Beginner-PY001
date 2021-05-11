# Python Strings

## What are we going to learn
*  

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
#ex4.0.8 String strip
text = " hello am 10 years old today "
print(text.strip(" "))
```
```python
#ex4.0.9 String Replace
text = " hello am 10 years old today "
print(text.replace("10", "12"))
```








The String Modulo Operator
```Python
'Get %d%% off on %s today only!' % (30, 'bananas')
print('Hello, my name is %s.' % 'Graham')
```
The String .format() Method: Arguments
```Python
print('%d %s cost $%.2f' % (6, 'bananas', 1.74))
```
Using keyword arguments
```Python
print('{quantity} {item} cost ${price}'.format(quantity=6,item='bananas',price=1.74))
```
```Python
x = "a"
print(f"Hey {x}")
```
## 003 Code Challenges
---
Use the previous code examples to help you complete the code challenges

### **Task 1-4**
1. Ask the user to enter their first name and surname and then output the length of their name
2. Building upon the code developed in the previous task now output on new lines the length of the users name, their name with a capital letter, their name all in lowercase
3. Building upon the previous code. Slice the first name and surname so that the first letter of the first name and surname is displayed in capitals


```Python
firstname = input("Enter your first name: ")
surname = input("Enter your surname:")

print((firstname[0:1]+surname[0:1]).upper())
```
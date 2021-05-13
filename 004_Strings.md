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
# string.find(substring, start, end)
x= "Hello Zander"
y = x.find("Zander", 6, 12)
print(y)
```
```python
#ex4.1.3 Using find with a conditional statement
x= "Hello Zander"
y = x.find("Zander")

if y >= 0:
  print("Match found")
else:
  print("Match not found")
```
```python
#ex4.1.4 find() is limited to strings 
x= ["a","b"]
y = x.find("a")
print(y)
```
```python
#ex4.1.5 index() example
# Syntax: string.index(substring, start, end) 
x= ["a","b","c"]
y = x.index("c")
print(y)
```
```python
#ex4.1.6 index() raise an error (ValueError)
x= ["a","b","c"]
y = x.index("d")
print(y)
```
```python
#ex4.1.7 Capture error
x= ["a","b","c"]
try:
    y.index("d")
except ValueError:
      print("Not found")
```
```python
#ex4.1.7 Count substring
x = "How may apples are there is an apple cart?"
y = x.count("apple")
print(y)
```

The String Modulo Operator
```Python
print('Hello, my name is %s.' % 'Graham')
print('Get %d%% off on %s today only!' % (30, 'bananas'))
```
The String .format() Method: Arguments
```Python
print('{} {} cost ${}'.format(6,'bananas',1.74))
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
# Python Strings

## What are we going to learn
*  

### Code Examples
---
```python
print("This is a string")
print("This is a \"string\"")
print('This is a \'string\'')
print("What about \\")
```
```python
num = 1
text = "I am"
print(text + " " + str(num))
```
```python
text = "I am 10 \nyears old today"
print(text)

text = """I am 10 
years old today"""
print(text)
```
```python
text = "I am 10 years old today"
print(len(text))

text = len("I am 10 years old today")
print(text)

text = "hello am 10 years old today"
print(text.capitalize())
print(text.upper())
print(text.lower())
print(text.title())

text = " hello am 10 years old today "
print(text.strip(" "))
```
Strings in Python are arrays of bytes
```Python
print ("Hello world"[0:2])
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
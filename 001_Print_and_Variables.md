# Introducing Python basics

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
print(x + y)
print(x - y)
print(x * y)
print(x / y)
```
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
# ex1.0.12
name = "zander"
number = 1
print(name + str(number))
```
```python
# ex1.1.013
number1 = "1"
number2 = 1
print(int(number1) + number2)
```
```python
# ex1.1.14
print("zander\npark")
```
```python
# ex1.1.15
name = "first name: zander"
surname = "surname: park"
print(name + "\n" + surname)
```

## 001 Code Challenges
---
Use the previous code examples to help you complete the code challenges
### **Task 1-4**
1. Get comfortable with your environment. Output hello world (if on Windows) using the command prompt start > CMD, the Python IDLE and in the Visual studio code editor terminal.
2. Create 2 new variables, name and surname. Print the variables so that they appear of individual lines.
3. Create a third variable, age. Print the age to appear below the surname
4. Create name, surname and age variables for a new person.
5. Calculate the total age of person 1 + person 2 and print the calculated value

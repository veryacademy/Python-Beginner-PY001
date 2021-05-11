# Introducing Python Basics

## Topics:

1. Taking input in Python
2. String Formatting - f-Strings

* Project - Pizza Slice Calculator
* Project - Age Calculator
* Project - Restaurant Bill Calculator

### Code Examples
---
```python
#ex2.0.1 Taking input in Python
textInput = input("Enter your first name: ")
```
```python
#ex2.0.2 Taking input in Python - with casting
numInput = int(input("Enter your age: "))
```
```python
#ex2.0.3 Input Errors
numInput = int(input("Enter your age: ")) # Type in a string to simulate an error
# Output:
# Traceback (most recent call last):
#   File "C:\example.py", line 1, in <module>
#     numInput = int(input("Enter your age: "))
# ValueError: invalid literal for int() with base 10: 'asd'
```
```python
#ex2.0.4 Taking input in Python - printing the output
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print(textInput + str(numInput))
```
```python
#ex2.0.5 Taking input in Python - Formatting the print output
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print("Name: " + textInput + "\n" + "Age: " + str(numInput))
```
```python
#ex2.0.6 String Formatting - f-Strings
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print(f"Name: {textInput} \nAge: {numInput}")
```

## 002 Code Challenges | Projects
---
Use the previous code examples to help you complete the code challenges
### **Challenges**

#### **1. Troubleshooting challenges**
Troubleshoot and fix the following code examples:

```python
# Troubleshooting Challenge 1
textInput = input("Enter your first name: ")
print(Hello + textInput)
```
```python
# Troubleshooting Challenge 2
age = input("Enter your age: ")
print(Age)
```
```Python
# Troubleshooting Challenge 3
textInput = input("Enter your first name: ")
numInput = input("Enter your age: ")
print(textInput + int(numInput))
```

#### **2. Pizza Slice Calculator**
Create a pizza slice calculator which will calculate the number of slices left to eat after the user enters the number of slices they have already eaten - assume the pizza has a maximum of 12 slices.

#### **3. Age Calculator**
Create an age calculator which will show users age on their next birthday.

#### **4. Customer Bill Calculator (Including Tax)**
Create a customer bill application to allow the waiter to input the name of the customer and their final bill total. Print to the screen the users details, the total before and after tax has been calculated.

```python
# Solution - Troubleshooting Challenge 1
textInput = input("Enter your first name: ")
print("Hello " + textInput)

# Solution - Troubleshooting Challenge 2 
age = input("Enter your age: ")
print(age)

# Solution - Troubleshooting Challenge 3
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print(textInput, str(numInput))
```


```python
# Challenge Solution - Pizza Slice Calculator
pizza = 12
slices = int(input("How many slices have you eaten?: "))
remaining = pizza - slices
print(f"Remaining pizza slices: {remaining}")
```

```python
# Challenge Solution: Age Calculator
textInput = input("Enter your first name: ")
age = int(input("Current Age: "))
ageAfterBirthday = age + 1
print("Name: {textInput} \nAge after next Birthday: {ageAfterBirthday}")
```

```python
# Challenge Solution: Customer Bill Calculator (Including Tax)
tax = 10
text_input = input("Enter your first name: ")
total_before_tax = int(input("The final bill total: "))
tax_to_pay = total_before_tax*tax / 100
total = (total_before_tax + tax_to_pay)

print("Name: {text_input} \nTotal(Before Tax): {total_before_tax} \nTax {tax_to_pay} \nTotal: {total}")

```tax 
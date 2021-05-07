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
#ex2.0.3 Taking input in Python - printing the output
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print(textInput + str(numInput))
```
```python
#ex2.0.4 Taking input in Python - Formatting the print output
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print("Name: " + textInput + "\n" + "Age: " + str(numInput))
```
```python
#ex2.0.5 String Formatting - f-Strings
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print(f"Name: {textInput} \nAge: {numInput}")
```

## 002 Code Challenges | Projects
---
Use the previous code examples to help you complete the code challenges
### **Challenges 1-4**

### Pizza Slice Calculator
Create a pizza slice calculator which will calculate the amount of slices left to eat after the user enters the number of slices they have already eaten - assume the pizza has a maximum of 12 slices.

### Age Calculator
Create an age calculator which will show users age on their next birthday.

### Customer Bill Calculator (Including Tax)
Create a customer bill application to allow the waiter to input the name of the customer and their final bill total. Print to the screen the users details, the total before and after tax has been calculated.

```python
pizza = 12
slices = int(input("How many slices have you eaten?: "))
remaining = pizza - slices
print(f"Remaining pizza slices: {remaining}")
```

```python
textInput = input("Enter your first name: ")
age = int(input("Current Age: "))
ageAfterBirthday = age + 1
print("Name: {textInput} \nAge after next Birthday: {ageAfterBirthday}")
```

```python
tax = 10
text_input = input("Enter your first name: ")
total_before_tax = int(input("The final bill total: "))
tax_to_pay = total_before_tax*tax / 100
total = (total_before_tax + tax_to_pay)

print("Name: {text_input} \nTotal(Before Tax): {total_before_tax} \nTax {tax_to_pay} \nTotal: {total}")

```
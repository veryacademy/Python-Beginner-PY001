# Introducing Python basics

### Code Examples
```python
#ex2.0.1
textInput = input("Enter your first name: ")
```
```python
#ex2.0.2
numInput = int(input("Enter your age: "))
```
```python
#ex2.0.3
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print(textInput + str(numInput))
```
```python
#ex2.0.4
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print("Name: " + textInput + "\n" + "Age: " + str(numInput))
```
```python
#ex2.0.5
textInput = input("Enter your first name: ")
numInput = int(input("Enter your age: "))
print("Name: {} \nAge: {}".format(textInput, numInput))
```

## 002 Code Challenges
---
Use the previous code examples to help you complete the code challenges
### **Task 1-4**
1. Create a pizza slice calculator which will calculate the amount of slices left to eat after the user enters the number of slices they have already eaten - assume the pizza has a maximum of 12 slices
2. Create an age calculator which will show users age on their next birthday
3. Create a customer bill application to allow the waiter to input the name of the customer and their final bill total. Print to the screen the users details, the total before and after tax has been calculated

```python
pizza = 12
slices = int(input("How many slices have you eaten?: "))
remaining = pizza - slices
print("Remaining pizza slices: {}".format(remaining))
```

```python
textInput = input("Enter your first name: ")
age = int(input("Current Age: "))
ageAfterBirthday = age + 1
print("Name: {} \nAge after next Birthday: {}".format(textInput, ageAfterBirthday))
```

```python
tax = 10
text_input = input("Enter your first name: ")
total_before_tax = int(input("The final bill total: "))
tax_to_pay = total_before_tax*tax / 100
total = (total_before_tax + tax_to_pay)

print("Name: {} \nTotal(Before Tax): {} \nTax {} \nTotal: {}".format(text_input, total_before_tax, tax_to_pay, total))

```
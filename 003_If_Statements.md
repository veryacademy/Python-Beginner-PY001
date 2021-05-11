# Introducing Python Basics

## Topics:

1. If
2. Whitespace / Indentation
3. Pass
4. Comparison Operators
5. The Boolean Data Type
6. Python Logical Operators
7. If..Else
8. If...Elif...Else
9. Nested If

* Challenge - Username / Password Checker
* Challenge - Coin Tiers
* Challenge - Pizza Slices - Continued

### Code Examples
---

```python
if condition:           
   # Statements to execute if
   # condition is true
    print("True")
```
```python
# Comparing two values, the expression is evaluated
# Python returns the Boolean answer (True or False)
if 1 == 1:
    print("True")
```
```python
# Using pass as placeholders
# if can not be empty
if b > a:
  pass
```

### Comparison Operators
---
* == Equal to and Both conditions must be met
* != Not equal to or Either condition must be met
* \> Greater than
* < Less than
* \>= Greater than or equal to
* <= Less than or equal to

```python
if 1 == 1:
    print("True")
# Outcome: True

if 1 != 2:
    print("True")
# Outcome: True

if 1 > 0:
   print("True")
# Outcome: True

if 1 < 10:
    print("True")
# Outcome: True

if 1 <= 10:
    print("True")
# Outcome: True

if 10 >= 10:
    print("True")
# Outcome: True
```
```Python
if "Hello" == "Hello":
    print("True")
# Outcome: True
```
```Python
x = "hello"
y = "hello"
if x == y:
    print("True")
# Outcome: True
```
### Booleans
---
```python
# Booleans represent one of two values: True or False.
x = True
y = False
print(f"{x},{y}")
```
```python
# They can also represent 1 and 0
x = int(False)
print(x)
x = int(True)
print(x)
```
```python
print(2 < 5)
```
```python
# Evaluate any value, and give you True or False in return
print(bool("Hello World"))
print(bool(1))
```
```python
if True:
    print("True")
```

### Python Logical Operators
---
Logical operators are used to combine conditional statements

```python
if True and True:
    print("True")
```
```python
if True or False:
    print("True")
```
```python
if 1 == 1 or 2 == 2 or 3 == 3:
    #True
    print("This is true once again!")
```

### If...Else
---
```python
if condition:
    # true-block
    # when the condition evaluates to True
else:
    # false-block
    # when the condition evaluates to False
```
```python
# Without else - program continues
if True:
    print("True")

print("Another Print")
```
```python
age = int(input("Enter your age: "))
requiredAge = 18

if age >= requiredAge:
	print("You may be legible for the course")
else: 
	yearsToGo = requiredAge % age
	print("Sorry you have " + str(yearsToGo) + " more years before you can start the course")
```

### If...elif...Else
---

```python
int = 15

if int == 1:
  print("This is true")
elif int == 5:
  print(str(int) + " is the number")
elif int == 15:
  print(str(int) + " is the number")
else: 
  print("Sorry we haven't matched the number")
```
```python
age = int(input("Enter your age: "))
requiredAge = 18

if age >= requiredAge and age < 60:
    print("you can start the course now")
elif age >= 60:
    print("you are eligible for discount on courses")
elif age == 30:
    print("you are eligible for half price courses")
else:
    years_to_go = requiredAge % age
    print(f"Sorry you have {years_to_go} more years to wait")
```
### Nested If
---

```python
age = int(input("Enter your age: "))
requiredAge = 18

if age >= requiredAge and age < 60:
    print("you can start the course now")

    if age == 30:
        print("you are eligible for discount on the courses")    

elif age >= 60:
    print("you are eligible for discount on courses")
else:
    years_to_go = requiredAge % age
    print(f"Sorry you have {years_to_go} more years to wait")
```
```python
int = 1000

if int >= 100:

  if int == 50:
      print(str(int) + " is the number")
  else:
      print("We couldn't work out the number")

elif int >= 1000:
  print(str(int) + " this number is way too big")
else: 
  print("Sorry lets try again")
```

### Short Hand
---
```python
# Short Hand If
if x > y: print("x is greater than y")
```
```python
# Short Hand If ... Else
x = 10
y = 20
print("x") if a > b else print("y")
```

## 003 Code Challenges
---
Use the previous code examples to help you complete the code challenges
### **Challenge 1 - Password Matching**

Create an application which will check the users password they enter to the password held in a variable. Write an output for both a failed and successful password match.

### Extension - Username Matching

Extending the password matching feature, only users who correctly enter the password and called by the name of zander should have access to the secret code! Extend the application to allow users to input their name as well as the password. If usernames and passwords match correctly print out - you have access, if not, let the user know they can not enter.

### **Challenge 2 - Coin Levels**

Create an application so that the user can enter the number of coins they have acquired. Based upon the amount of coins entered, the application will determine the user level. Bronze if coins equal 0-20, Silver if the coins entered equals 21-40 and Gold 41+. The programme will output the level name (Bronze, Silver or Gold) to the user based upon the coins entered.

### **Challenge 3 - Pizza Slices - Continued**
In the previous challenged we created a pizza slice calculator which will calculate the amount of slices left to eat after the user enters the number of slices they have already eaten - assuming the pizza has a maximum of 12 slices. The problem with this application is that if the user types in more than 12 or less than 0 slices we are presented with a number which is not ideal. For example if the user types in 13 the outcome is -1 slices.

Let's now extend the original application to include a method of capturing the users input to check for numbers out of range. For example we need to validate the number that the users enters so that if the user enters a number below 0 or more than 12 the application will return a message to the user that they have entered a wrong number. The application should only be able to calculate pizza slices when numbers 0-12 have been entered by the user.

#### Original Code:

```python
pizza = 12
slices = int(input("How many slices have you eaten?: "))
remaining = pizza - slices
print(f"Remaining pizza slices: {remaining}")
```

### Solutions
---

```python
# Challenge 1 Solution - Matching passwords
x = "notsafe"
y = input("Enter your password: ")

if x == y:
	print("Correct password entered")
else: 
    print("Sorry, please try again")
```
```python
# Extension Solution - Username Matching 
pw = "notsafe"
username = "zander"

y = input("Enter your username: ")
z = input("Enter your password: ")

if y == username and z == pw:
	print("You have access")
else: 
    print("Sorry, please try again")

```
```python 
# Challenge 2 Solution - Coin Challenge
x = int(input("Amount of coins: "))

if x >= 0 and x <= 20:
    print("Bronze")
elif x >= 21 and x <= 40:
    print("Silver")
elif x >= 41:
    print("Gold")
else:
    print("Sorry type in a correct number")
```
```python 
# Challenge 3 Solution - Pizza slices 
pizza = 12
slices = int(input("How many slices have you eaten?: "))

if slices < 0 or slices > 12:
    print("Sorry you entered the wrong amount")
else:
    remaining = pizza - slices
    print(f"Remaining pizza slices: {remaining}")
```
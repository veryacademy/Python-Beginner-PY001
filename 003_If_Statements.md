# Python If statements

## Topics:

1. If
2. If..Else
3. If..Elif..Else

* Project - Pizza Slice Calculator

### Code Examples
---

```python
if condition:           
   # Statements to execute if
   # condition is true
    print(True)

# Comparing two values, the expression is evaluated
# Python returns the Boolean answer (True or False)
if 1 == 1:
    print("True")
```

Comparison Operators
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
```python
# Booleans represent one of two values: True or False.
x = True
y = False
print(r"{x},{y}")
```
```python
# They can also represent 1 and 0
x = int(False)
print(x)
x = int(True)
print(x)
```
```python
# Evaluate any value, and give you True or False in return
print(bool("Hello World"))
print(bool(1))
```
```python
x = 1
if x:
    print("True")
```
```python
if True:
    print("True")
```


```python
if True and True:
    #True
    print("This is true again!")
```
```python
if True or False:
    #True
    print("This is true once again!")
```
```python
if 1 == 1 or 2 == 2 or 3 == 3:
    #True
    print("This is true once again!")
```
```python
if False:
  #True
  print("This is true")
else: 
  print("Sorry this is incorrect")
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
```python
int = 15

if int == 1:
  #True
  print("This is true")
elif int == 5:
  print(str(int) + " is the number")
else: 
  print("Sorry we haven't matched the number")
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
## 003 Code Challenges
---
Use the previous code examples to help you complete the code challenges
### **Task 1-4**
1. Create an application which will check the users password they enter to the password held in a variable. Write an output for both a failed and successful password match
2. Only users who correctly enter the password and called by the name of zander should have access to the secret code! Write a program to take the age and name as input and validate their details. If users match correctly print out - you have access, not not, let the user know they can not enter
3. The user should be able to enter a number of coins they have. Based upon the amount of coins the programme will determine the level Bronze if coins equal 0-20, Silver if the coins entered equals 21-40 and Gold 41+. The programme will output the level to the user based upon the coins entered

```python
password = "notsafe"
enterPassword = input("Enter your password: ")

if password == enterPassword:
	print("Correct password entered")
else: 
  print("Sorry, please try again")
```
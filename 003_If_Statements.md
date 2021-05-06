# Python If statements

## What are we going to learn
*  
Comparison Operators
* == Equal to and Both conditions must be met
* != Not equal to or Either condition must be met
* \> Greater than
* < Less than
* \>= Greater than or equal to
* <= Less than or equal to
Logical Operators
* and Both conditions must be met
* or Either condition must be met

### Code Examples
---
```python
if 1 == 1:
    #True
    print("This is true")
if 1 != 2:
    #True
    print("This is true")
if 1 > 0:
    #True
    print("This is true")
if 1 < 10:
    #True
    print("This is true")
if 1 <= 10:
    #True
    print("This is true")
if 10 >= 10:
    #True
    print("This is true")
```
```python
# Boolean 
# True False
check1 = int(False)
print(check1)
check2 = int(True)
print(check2)
```
```python
if check2:
    #True
    print("This is true")
```
```python
if True:
    #True
    print("This is true of course!")
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
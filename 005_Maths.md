# Python Strings

## What are we going to learn
  
* \+ Addition
* \- Subtraction
* \* multiplication
* ** Power
* // Whole number division
* % Finds the remainder

### Code Examples
---
```python
print(1+0)
print(2-1)
print(3*37)
print(10.536**2)
print(10//6)
print(10%3)
```
```Python
import math
print(math.sqrt(4))
pi = math.pi
print(pi)
```
```Python
num1 = float(1.2312321)
num2 = int(1)
num3 = num1 + num2
print(num3)
print( round(num1,2) )
```
```Python
check_int = isinstance(num1, int)
print(check_int)

if check_int:
    print("Float detected")
else:
    print("Float not detected")
```
How Do I Remember It All ... ? BODMAS !

B

Brackets first

O

Orders (i.e. Powers and Square Roots, etc.)

DM

Division and Multiplication (left-to-right)

AS

Addition and Subtraction (left-to-right)

```Python
print(1+10*10) # M-A = 101
print(10*1+10) # M-A = 20
print(10*(1+10)) # B-M = 110
print(10/2*(1+10)) # B-D-M = 55
```

## 005 Code Challenges
---
Use the previous code examples to help you complete the code challenges

### **Task 1-4**
1. By default python shows PI to 15 places. Using round print PI to output with only 2 decimal places.
2. Create a product sales calculator. The user will input a price of a product and the programme should calculate the price of the product minus the sale discount of 10%.
3. If you haven't done so already, using hte BODMAS principle create the calculation for the discounted price with one calculation.
4. Ask the user to enter the radius of a circle
(centre point to the edge). The programme should work out the area of the circle (π*radius2). Round the answer to two decimal places.
5. Build a simple calculator that allows user to type in two numbers and the operation that they wish to perform, + - / or *. Perform the calculation and print the result.

```Python
original = float(input("Enter the amount: "))
discount = original / 100 * 10
# Format Converts to string
newprice = format(original - discount, '.2f')
print("£" + str(newprice))
print("£" + newprice)
```
```Python
original = float(input("Enter the amount: "))
discount = original - original / 100 * 10 
# Format Converts to string
newprice = format(discount, '.2f')
print("£" + newprice )
```
```Python
import math
radius = int(input("Enter the radius: "))
area1 = round(math.pi*(radius**2), 2)
# or
area2  = format(math.pi*(radius**2), '.2f')
print("The area: " + str(area1))
print("The area: " + str(area2))
print("The area: {}".format(area1))
print('The area: %s %s' % (area1, 'well done'))
```
```Python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
choice = input("Enter the operation +,-,/,*: ")

if choice == "+":
    result = num1 + num2
if choice == "-":
    result = num1 - num2
if choice == "/":
    result = num1 / num2
if choice == "*":
    result = num1 * num2

print(result)
```
# Python Introducing numbers and math

## Topics:
* Simple calculations
* Shorthand combinations
* Order of operations
* Number rounding
* Python math library

### Code Examples
---
```python
# ex5.0.1 Simple calculations
print(1+0)
print(2-1)
print(3*37)
print(10.536**2)
print(10//6)
print(10%3)
```
```Python
# ex5.0.2 Performing simple calculations
x = float(1.2312321)
y = int(1)
z = x + y

check = isinstance(z, float)
print(check)
print(z)
```
```Python
# ex5.0.3 Shorthand combinations
# Assignment Operators besides the = operator
x = 1
x += 2
x -= 2
x *= 2
print(x)
```
```python
# ex5.0.4 Order of operations
B - Brackets first
O - Orders (i.e. Powers and Square Roots, etc.)
DM - Division or Multiplication (left-to-right)
AS - Addition or Subtraction (left-to-right)

print(1+10*10) # M-A = 101
print(10*1+10) # M-A = 20
print(10*(1+10)) # B-M = 110
print(10/2*(1+10)) # B-D-M = 55
```
```Python
# ex5.0.5 Number rounding
x = 1.45123123
print(round(x,2))
print(format(x,'.2f'))
print("Price" + format(x,'.2f')) # Converts to string
```
```Python
# ex5.0.6 Python math library
import math
x = math.pi
print(x)
x = math.sqrt(4)
print(x)
```

## 005 Code Challenges
---
Use the previous code examples to help you complete the code challenges

### **Task 1-4**
1. By default python shows PI to 15 places. Using round print PI to output with only 2 decimal places.
2. Create a product sales calculator. The user will input a price of a product and the programme should calculate the price of the product minus the sale discount of 20%.
3. If you haven't done so already, using the BODMAS principles create the calculation for the discounted price with one calculation.
4. Ask the user to enter the radius of a circle
(centre point to the edge). Print out the area of the circle (π*radius2). Round the answer to two decimal places.
5. Build a simple calculator that allows user to type in two numbers and the operation that they wish to perform, + - / or *. Perform the calculation and print the result.

### Solutions
---
```Python
# Challenge 1 Solution
import math
x = math.pi
print(round(x,2))
```
```Python
original = float(input("Enter the amount: "))
discount = original / 100 * 10
newprice = format(original - discount, '.2f')
print("£" + str(newprice))
print("£" + newprice)
```
```Python
original = float(input("Enter the amount: "))
discount = original - original / 100 * 10 
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
x = float(input("Type in a number: "))
y = float(input("Type in another number: "))
z = input("+ - / *: ")

if z == "+":
  print(x + y)
elif z == "-":
  print(x - y)
elif z == "/":
  print(x / y)
elif z == "*":
  print(x * y)
else:
  print("you did not type in a correct operator")
```
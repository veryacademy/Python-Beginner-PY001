# Functions
Functions are blocks of code which perform specific tasks and can be called upon at any time in the program to run that code.

### Advantages
* You can write a block of code and it can be used and reused
at different times during the program.
* It makes the program simpler to understand as the code
is grouped together into chunks.

### Code Examples
---
```python
# Function
def print_username():
    username = input("Enter your username: ")
```
```Python
# Initiate function
def print_username():
    username = input("Enter your username: ")

print_username()
```
```Python
def get_username():
    username = input("Enter your username: ")
    return username

def main():
    username = get_username()
    print(username)

main()
```
```Python
# Phase 1
def get_bill_total():
    bill_total = float(input("Enter the amount: "))
    return bill_total

def main():
    total = get_bill_total()
    discount = total - total / 100 * 10 
    final_price = format(discount, '.2f')
    print("£" + final_price )

main()
```
```Python
def calculate_discount(total):
    discount = total - total / 100 * 10 
    return discount

def get_bill_total():
    bill_total = float(input("Enter the amount: "))
    final_total = format(calculate_discount(bill_total),'.2f')
    return final_total

def main():
    total = get_bill_total()
    print("£" + total )

main()
```

### **Task 1-4**
1. Convert the following example we previously built so that the radius calculation is performed in a separate function.

```Python
import math
radius = int(input("Enter the radius: "))
area1 = round(math.pi*(radius**2), 2)
```
2. We made an example to calculate the total cost of an item once the discount has been applied. See code example below. Change amount of discount applied based upon the amount spent. For example if the customer spends 100 or more the discount applied should be 20% if the customer spends less than 100 the discount applied should be 10%

```Python
def calculate_discount(total):
    discount = total - total / 100 * 10 
    return discount

def get_bill_total():
    bill_total = float(input("Enter the amount: "))
    final_total = format(calculate_discount(bill_total),'.2f')
    return final_total

def main():
    total = get_bill_total()
    print("£" + total )

main()
```
```Python
import sys

def calculate_discount_percentage(total):
    if total >= 100:
        discount = 20
    elif total > 0 and total < 100:
        discount = 10
    return discount

def calculate_discount(total):
    discount_percentage = calculate_discount_percentage(total)
    discount = total - total / 100 * discount_percentage 
    return discount

def get_bill_total():

    try:
        bill_total = float(input("Enter the amount: "))
    except ValueError as e:
        print ('Incorrect value entered')
        # quit() This function (callable instance objects) should only be used in the interpreter.
        # exit()
        sys.exit()
    
    if bill_total < 1:
        print ('Incorrect value entered')
        sys.exit()

    final_total = format(calculate_discount(bill_total),'.2f')
    return final_total

def main():
    total = get_bill_total()
    print("£" + total )

main()
```
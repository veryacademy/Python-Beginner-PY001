# Functions
Functions are blocks of code which perform specific tasks and can be called upon at any time in the program to run that code.

### Code Examples
---
```python
# 10.0.1 Create a function
def print_username():
    username = input("Enter your username: ")
```

```Python
# 10.0.2 Run a function
def print_username():
    username = input("Enter your username: ")

print_username()
```

```Python
# 10.0.3 Calling a function from an existing function
def get_username():
    username = input("Enter your username: ")
    return username

def main():
    username = get_username()
    print(username)

main()
```

```Python
# 10.0.4 Function arguments
def name(name):
  print(f"Your name is: {name}")

name("Ali")
name("Sheeba")
```

```python
# 10.0.5 Multiple arguments
def name(fname, sname):
  print(f"Your name is: {fname} {sname}")

name("Ali", "Ahmed")
name("Sheeba", "James")
```

```Python
# 10.0.6 Function Example
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
# 10.0.7 Function Example
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

## 010 Code Challenges
---
Use the previous code examples to help you complete the code challenges

### **Challenge 1 - Radius calculation**
Convert the following example we previously built so that the radius calculation is performed in a separate function.

```Python
import math
radius = int(input("Enter the radius: "))
area1 = round(math.pi*(radius**2), 2)
```

### **Challenge 2 - Cost Calculation**
We made an example to calculate the total cost of an item once the discount has been applied. See code example below. 

1. Change amount of discount applied based upon the amount spent. For example if the customer spends 100 or more the discount applied should be 20% if the customer spends less than 100 the discount applied should be 10%
2. Use Try/Except to capture if the user accidentally types in the wrong input

```Python
# Original Code
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


### Solutions
---

```Python
# Challenge 2 - Cost Calculation
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
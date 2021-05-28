# While Loop
A while loop allows code to be repeated an unknown number of times as long as a condition is being met.

### Code Examples
---
```python
# 9.0.1 A while loop
i = 1
while i < 6:
  print(i)
  i += 1
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
# 9.0.2 Random Number 
import random
count=0
num = ''
rand = str(random.randint(1,10))

while num != rand:
    num = input("Enter a number between 1-10:" )
    count +=1

print(rand)
print(f"Guess Count {count}")
print("Correct!")
```
```python
# 9.0.3 Break
import random
num = 1
while num > 0:
    print(num)
    num = random.randint(1,10)
    if num == 5:
        break
print("5 was found")
```
```python
# 9.0.4 Else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("Finished")
```
```python
i = 1
while i < 10:
  print(i)
  i += 1

  if i == 8:
      break

else:
  print("Finished")
```
```python
i = 1
while i < 10:
    print(i)

    i += 1

    if i == 4:
        continue
    else:
        print("next")

else:
    print("Finished")
```

## 009 Code Challenges
---
Use the previous code examples to help you complete the code challenges

### **Challenge 1 - Counting**
Write a while loop that adds all the numbers from 1 to 100

### **Challenge 2 - List Iteration**
Take the following list: 
```python
numbers=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]
```
Using a while loop iterate through the list and for every instance of 100 print out "Found one!"

### **Challenge 3 - Appending a list**
Using the following list of names:
```python
names=["Joe", "Sarah"]
```
Using a while loop allow users to add new names to the list indefinitely. Each time a user adds a new name ask the user if they would like to add another name. 1 = yes and 2 = no. The programme should stop if the users selects 2, no.

### **Challenge 4 - Dice Roll Simulator**
Create a dice roll simulator whereby the user is first given an option on screen to either play or exit the simulator. An input() function is used to capture the users choice.

```
1. Roll the dice
2. Exit Game
Choose 1 or 2:
```

On the user selecting option 1, the simulator should produce a number between 1 and 6. 

```
====
Dice Roll: 4
====
```

After which, the application should loop back to the introduction screen where the user is asked to choose option 1 or 2 once more. If the user selects option 2, the simulator should exit/stop. 

```
1. Roll the dice
2. Exit Game
Choose 1 or 2:
```

### Solutions
---

```python
# Challenge 1 - Counting
num = 1
while num <= 100:
    print(num)
    num +=1
```
```python
# Challenge 2 - List Iteration
numbers=[100, 84, 68, 35, 42, 100, 65, 66, 76, 11, 35, 13, 100, 80, 95]
  
length = len(numbers)
i = 0
  
while i < length:

    if numbers[i] == 100:
        print("Found one!")

    i += 1
```
```python
# Challenge 3 - Appending a list
names=["Joe", "Sarah"]
    
while True:

    names.append(input("Add a new name: "))
    print(names)
    x = int(input("Another name 1-yes 2-no: "))

    if x == 2:
        break
```
```Python
# Challenge 4 - Dice Roll Simulator
import random 
while True:     
     print("1. Roll the dice\n2. Exit Game")    
     user = int(input("Choose 1 or 2: "))     
     if user==1:         
        number = random.randint(1,6)         
        print(f"====\nDice Roll: {number}\n====")     
     else:      
        break
```
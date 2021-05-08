# While Loop
A while loop allows code to be repeated an unknown number of times as long as a condition is being met.

## What are we going to learn

### Code Examples
---
```python
import random
num = ''
rand = str(random.randint(1,10))

while num != rand:
    num = input("Enter a number between 1-10:" )

print(rand)
print("Correct!")
```
```python
i = 1
while i < 6:
  print(i)
```
```python
i = 1
while i < 6:
    i+=1
    print(i)
```
```python
import random
num = 1
while num > 0:
    print(num)
    num = random.randint(1,10)
    if num == 5:
        break
print("5 was found")
```

## 009 Code Challenges
---
Use the previous code examples to help you complete the code challenges
### **Challenge 1 - Dice Roll Simulator**
Create a dice roll simulator whereby the user is first give an option on screen to either play or exit the simulator. An input() function is used to capture the users choice.

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

```Python
# Challenge 1 - Dice Roll Simulator
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
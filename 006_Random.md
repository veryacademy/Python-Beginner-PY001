# Random
Python can generate random values. In reality, the values are not
completely random as no computer can cope with that; instead it uses an incredibly complex algorithm that makes it virtually impossible to accurately predict its outcome so, in effect, it acts like a random function.

* Random numbers within a specified range;
* A random choice from a range of items that are input.

## What are we going to learn

### Code Examples
---
```python
import random
Random float between 0.0 and 1.0
num = random.random()
print(num)
```
Random int
```python
import random
num = random.randint(0,100)
print(num)
```
Random float
```python
import random
num = random.uniform(1.1, 10.1)
print(num)
```
Integer from 0 to 9 inclusive
```python
import random
num = random.randrange(10)
print(num)
```
Even integer from 0 to 100
```python
import random
num = random.randrange(0, 101, 2)
print(num)
```
```python
import random
item_list = ["rock","paper","scissors"]
selection = random.choice(item_list)
print(selection)
```

### **Task 1-4**
1. Create a random number game. Ask the user to input a number between 1 and 10. Generate a random number between 1 and 10 and check to see if the users and random number matches. If the do notify the user they have won, else ask the user to try again.
2. Create a rock, scissors, paper game.

```python
import random

num = input("Select a number between 1 and 10: ")
rand = random.randint(1,10)

print("Your number: " + str(num))
print("CPU number: " + str(rand))
if int(num) == rand:
    print("You Win!")
else:
    print("Try again")
```
```python
import random
item_list = ["rock","paper","scissors"]

choice = input("Type your selection (rock, paper, scissors): ")
randomchoice = random.choice(item_list)
print("CPU Choice:" + randomchoice)
if choice == "rock":
    if randomchoice == "rock":
        print("Draw")
    elif randomchoice == "paper":
        print("You lose")
    elif randomchoice == "scissors":
        print("You win")
elif choice == "paper":
    if randomchoice == "rock":
        print("You win")
    elif randomchoice == "paper":
        print("Draw")
    elif randomchoice == "scissors":
        print("You lose")
elif choice == "scissors":
    if randomchoice == "rock":
        print("You lose")
    elif randomchoice == "paper":
        print("You win")
    elif randomchoice == "scissors":
        print("Draw")
else:
    print("You did not enter a valid option")
```
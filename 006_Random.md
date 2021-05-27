# Python Random
Python can generate random values. In reality, the values are not
completely random as no computer can cope with that; instead it uses an incredibly complex algorithm that makes it virtually impossible to accurately predict its outcome so, in effect, it acts like a random function.

## Topics:
* Random numbers within a specified range
* A random choice from a range of items that are input

### Code Examples
---
```python
# ex6.0.1 Random float between 0.0 and 1.0
import random
num = random.random()
print(num)
```
```python
# ex6.0.2 Random integer
import random
num = random.randint(0,100)
print(num)
```
```python
# ex6.0.3 Random float
import random
num = random.uniform(1.1, 10.1)
print(num)
```
```python
# ex6.0.4 Integer range
import random
num = random.randrange(10)
print(num)
```
```python
# ex6.0.5 Integer range (Even integer from 0 to 100)
import random
num = random.randrange(0, 101, 2)
print(num)
```
```python
import random
# ex6.0.6 Random letter selection 
x = 'zander'
y = random.choice(x)
print("random letter chosen is: ", y)
```
```python
import random
# ex6.0.7 Random list selection 
item_list = ["rock","paper","scissors"]
selection = random.choice(item_list)
print(selection)
```
```python
import random
# ex6.0.8 Random sample 
x = [1,2,3,4,5,6,7,8]
y = random.sample(x, 2)
print(y)
# space
print(*y)
# comma
print(*y, sep = ", ") 
# new line
print(*y, sep = "\n")
# integers to string
print (str(y)[1:-1])
```

## 006 Code Challenges
---

### **Task 1-3**
1. Create a random number game. Ask the user to input a number between 1 and 10. Generate a random number between 1 and 10 and check to see if the users and random number matches. If the do notify the user they have won, else ask the user to try again.
2. Create a rock, scissors, paper game.
3. Create a Lottery Picker which picks and prints 6 numbers from the list provided.

### Solutions
---

```python
# Challenge 1 Solution
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
# Challenge 2 Solution
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
```python
# Challenge 3 Solution
import random

x = [1,2,3,4,5,6,7,8,9,10]
y = random.sample(x, 6)
print(*y)
```
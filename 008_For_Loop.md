# For Loop
A for loop allows Python to keep repeating code a set number of times. It is sometimes known as a counting loop because you know the number of times the loop will run before it starts.

### Code Examples
---
```python
# ex8.0.1 Iterate over a string
for i in "hello":
    print(i)
```
```python
# ex8.0.2 Iterate over a list
x = ('a','b','c')
for i in x:
    print(i)
```
```python
# ex8.0.3 Iterate over a dictionary 
x = {1:'a',2:'b',3:'c'}
for i in x:
# for i in x.values():
# for i, v in words.items():
#   print(i, v)
    print(i)
```
```python
# ex8.0.3 Iterate with range
for i in range(10,0,-1):
    print(i)

for i in range(0,10,2):
    print(i)

for i in range(10,0,-2):
    print(i)

for i in range(0,4):
    x = input("Give me a number: ")

    if x == "10":
        print("yay you got it right!")
```
```python
# ex8.0.4 Stop iterations
x = (1,2,3,4,5,6)
for i in x:
    print(i)
    if i == 4:
        break
    # print(i)
```
```python
# ex8.0.4 Continue
x = (1,2,1,2,1,2)
for i in x:
    if i == 1:
        continue
    print(i)
```
```python
# ex8.0.5 Else
x = (1,2,1,2,1,2)
for i in x:
    print(i)
else:
    print("Finished")
```
```python
# ex8.0.6 Nested Loops
a = (1,1,1,1,1,1)
b = (2,2,2,2,2,2)
for x in a:
    print(x)
    for y in b:
        print(y)

a = (1,1,1,1,1,1)
b = (2,2,2,2,2,2)
for x in a:
    for y in b:
        print(x, y)
```

## 008 Code Challenges
---
Use the previous code examples to help you complete the code challenges:

1. Let's put our new knowledge to the test by creating a number guessing game. First randomly create a number between 1-20, or your preferred range. Now let's ask the user to type in a number between the number range we have selected. The user should be given 4 turns or chances to guess the number. 

Just before the last guess print:

```
This is your last guess!...
```

Display a message if the user guesses the right number:

```
You guessed correctly! 
The right number was 2
```

If the user does not guess within 4 turns, display a message:

```
====
Sorry! The number was 12
====
```

2. In the previous modules we have built a Rock, Paper, Scissors game. Let's now expand and adapt the game so that the winner is the best of 3 games, the first person, the user or the ComputerAI to win 2 games win overall. 

### Solutions
---

```python
# Challenge 1 Solution
import random
x = random.randint(1,20)
for i in range(0,4):
    y = int(input("Guess the number between (1-20): "))
    if i == 2:
        print("This is your last guess!...")
    if x == y:
        print("You guessed correctly! ")
        print(f"The right number was {x}")
        break
if y != x:
    print(f"====\nSorry! The number was {x}\n====")
```
```python
import random
item_list = {1:"rock",2:"paper",3:"scissors"}

ai_score = 0
user_score = 0

for x in range(0,4):

    if ai_score == 2:
        print("=====")
        print("AI Wins")
        print("=====")
        break
    elif user_score == 2:
        print("=====")
        print("User Wins")
        print("=====")
        break
    elif x == 3:
        print("=====")
        print("The game is a draw")
        print("=====")
        break

    try:
        choice = int(input("Type your selection (1 - rock, 2 - paper, 3 -scissors): "))
    except ValueError:
        print("=====")
        print("You did not enter a valid option - please try again")
        print("=====")
        break
    
    random_choice = random.choice(list(item_list.values()))

    if item_list[choice] == random_choice:
        print("Draw")

    if item_list[choice] == "rock":
        if random_choice == "paper":
            print("You lose")
            ai_score += 1
        elif random_choice == "scissors":
            print("You win")
            user_score += 1
    elif item_list[choice] == "paper":
        if random_choice == "rock":
            print("You win")
            user_score += 1
        elif random_choice == "scissors":
            print("You lose")
            ai_score += 1
    elif item_list[choice] == "scissors":
        if random_choice == "rock":
            print("You lose")
            ai_score += 1
        elif random_choice == "paper":
            print("You win")
            user_score += 1

```

### **Troubleshooting challenges**
Troubleshoot and fix the following code examples:

```python
# Troubleshooting Challenge 1
x = ('1','2','3','4','5','6')
for i in x:
    print(i)
    if i == 4:
        break
```
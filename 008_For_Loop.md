# For Loop
A for loop allows Python to keep repeating code a set number of times. It is sometimes known as a counting loop because you know the number of times the loop will run before it starts.

## What are we going to learn

### Code Examples
---
```python
for i in range(0,10):
    print(i)
```
```python
for i in range(10,0,-1):
    print(i)
```
```python
for i in range(0,10,2):
    print(i)
```
```python
for i in range(10,0,-2):
    print(i)
```
```python
word = "hello"
for i in word:
    print(i)
```
```python
for i in word[0:1]:
    print(i)
```
```python
word = input("Enter your name: ")
for i in word:
    print(i)
```
```python
words = ["apple","banana","pear"]
for i in words:
    print(i)
```
```python
words = {1:"apple",2:"banana",3:"pear"}
for i in words:
    print(i)
```
```python
words = {1:"apple",2:"banana",3:"pear"}
for i in words.values():
    print(i)
```
```python
for i, v in words.items():
  print(i, v)
```

## 009 Code Challenges
---
Use the previous code examples to help you complete the code challenges
### **Challenge 1 - Guess the number game**
Let's put our new knowledge to the test by creating a number guessing game. First randomly create a number between 1-20, or your preferred range. Now let's ask the user to type in a number between the number range we have selected. The user should be give 4 turns or chances to guess the number. 

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

### Solutions
---

```python
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
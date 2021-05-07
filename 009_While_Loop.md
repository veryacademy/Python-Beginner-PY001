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
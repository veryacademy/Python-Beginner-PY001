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
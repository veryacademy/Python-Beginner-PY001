# Python Structured Data (Tuples, Lists and Dictionaries)
So far, we have used variables that can store a single item of data in them. Python provides 4 built-in data types that we can use to store collections of data, Tuple, List, Set, and Dictionary, each all having different features.

## Topics:

### Tuples
Once a tuple is defined you cannot change what is stored in it. A tuple is a collection that is ordered and Immutable (can not be changed) Tuples are written with round brackets.

### List 
The contents of a list can be changed while the program is running and lists are one of the most common ways to store a collection of data under one variable name in Python. List items are ordered, changeable, and allow duplicate values.

### Dictionaries
The contents of a dictionary can also be changed while the program is running. Each
value is given an index or key you can define to help identify each piece of data. This index
will not change if other rows of data are added or deleted, unlike lists where the position of
the items can change and therefore their index number will also change.


### Code Examples
---
```python
# ex7.0.1 # Tuple with stings
item_tuple = ("rock","paper","scissors")
print(item_tuple)
print(item_tuple.index("rock"))
print(item_tuple.index("paper"))
print(item_tuple[0])
print(item_tuple[1])
```
```python
# ex7.0.2 # Tuple with Numbers
item_tuple = (1,2,3)
print(item_tuple)
print(item_tuple[0])
print(item_tuple[1])
```



```python
item_list = ["rock","paper","scissors"]
print(item_list)
print(item_list[1])
print(item_list[2])
```
```python
item_list.append(input("Add a new item: "))
print(item_list)
```
```python
print(len(item_list))
```
```python
print(sorted(item_list))
```
```python
print(type(item_list))
print(type(item_list[0]))
```
Dictionary
```python
item_dictionary = {1:"rock",2:"paper",3:"scissors"}
print(type(item_dictionary))
print(type(item_dictionary[1]))
print(item_dictionary[1])
print(item_dictionary[2])
```
Add single item
```python
item_dictionary = {1:"rock",2:"paper",3:"scissors"}
item_dictionary[1] = "sock"
print(item_dictionary[1])
```
Add multiple
```python
item_dictionary = {1:"rock",2:"paper",3:"scissors"}
item_dictionary[4] = 'sock'
item_dictionary.update({5:'shoe',6:True})
print(item_dictionary)
```
Delete
```python
item_dictionary = {1:"rock",2:"paper",3:"scissors"}
item_dictionary.pop(1,None)
print(item_dictionary)
```
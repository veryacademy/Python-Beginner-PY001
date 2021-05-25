# Python Structured Data
So far, we have used variables that can store a single item of data in them. Python provides 4 built-in data types that we can use to store collections of data, Tuple, List, Set, and Dictionary, each all having different features.

## Topics:

* Tuples
* List 
* Dictionaries

### Code Examples
---

```python
# ex7.0.1 Tuple with stings
item_tuple = ("rock","paper","scissors")
print(item_tuple)
print(item_tuple.index("rock"))
print(item_tuple.index("paper"))
print(item_tuple[0])
print(item_tuple[1])
```
```python
# ex7.0.2 Tuple with Numbers
item_tuple = (1,2,3)
print(item_tuple)
print(item_tuple[0])
print(item_tuple[1])
```
```python
# ex7.0.3 Tuple Errors
# Must include a trailing comma if 1 item
item_tuple = (1,)
print(item_tuple)
# Error - Tuple is immutable
item_tuple[0] = 1
print(item_tuple)
```
```python
# ex7.0.4 Loop and print a tuple
item_tuple = (1,2,3)
for item_tuple in item_tuple:
  print(item_tuple)
```
```python
# ex7.0.5 Over write a tuple
items = (1, 2)
print("Original Numbers:")
for items in items:
  print(items)
items = (3, 4)
print("\nModified Numbers:")
for items in items:
  print(items)
```

### List
---

```python
# ex7.0.6 List with strings
item_list = ["rock","paper","scissors"]
print(item_list)
print(item_list[0])
print(item_list[1])
print(item_list[2])
print(item_list.index("rock"))
```
```python
# ex7.0.7 Lists can contain different data types
item_list = [1,2,"zander"]
print(item_list)
print(item_list[0])
print(item_list[1])
print(item_list[2])
print(item_list.index(1))
```
```python
# ex7.0.7 Length of list
item_list = [1,2,"zander"]
print(len(item_list))
```
```python
# ex7.0.8 Create a list using the list() Constructor
new_list = list(("a", "b", "c")) # double round-brackets
print(new_list)
```
```python
# ex7.0.9 last item and range of indexes
item_list = [1,2,"zander"]
print(item_list[1:2])
print(item_list[-1])
```
```python
# ex7.1.0 Check items in list
item_list = [1,2,"zander"]
if "zander" in item_list:
  print(f"Hello zander")
```
```python
# ex7.1.1 Add new item to list
item_list = [1,2,"zander"]
item_list.append(input("Add a new item: "))
print(item_list)
```
```python
# ex7.1.2 Change items in list
item_list = [1,2,"zander"]
item_list[0] = 10 
print(item_list)
```
```python
# ex7.1.3 Remove item in list
item_list = [1,2,"zander"]
item_list.remove(1)
item_list.remove(input("Remove item: "))
print(item_list)
```
```python
# ex7.1.4 Print list items one by one
item_list = [1,2,3]
for x in item_list:
  print(x)
```
```python
# ex7.1.5 Sorting a list
item_list = [1,2,3]
print(sorted(item_list))
```
```python
# ex7.1.6 Insert into list
item_list = [1,2,"zander"]
item_list.insert(0, "first item")
print(item_list)
```

### Dictionary
---

```python
# ex7.1.7 Dictionaries store data values in key:value pairs
item_dictionary = {1:"rock",2:"paper",3:"scissors"}
print(type(item_dictionary))
print(type(item_dictionary[1]))
print(item_dictionary[1])
print(item_dictionary[2])
```
```python
# ex7.1.8 Add, replace and delete data
item_dictionary = {1:"rock",2:"paper",3:"scissors"}
item_dictionary[1] = "sock" # Replace
item_dictionary.update({5:'shoe',6:True}) # Add new data (any data type)
item_dictionary.pop(1,None) # delete
print(item_dictionary)
print(len(item_dictionary))
print(type(item_dictionary))
```

## 007 Code Challenges
---
1. In the previous module we built a rock paper scissors game. Let's first replace the list used to store the values Rock, Paper and Scissors with a dictionary. Ask the user to select 1,2 or 3 to select Rock Paper or Scissors so that they no longer have to type in the word when the game starts.

### Solutions
---

```python
# Challenge 1 Solution
import random
item_list = {1:"rock",2:"paper",3:"scissors"}

choice = int(input("Type your selection (1 - rock, 2 - paper, 3 -scissors): "))
random_choice = random.choice(list(item_list.values()))

# random_choice = random.choice(list(item_list.key()))
# random_choice = random.choice(list(item_list.items()))

print(f"CPU Choice: {random_choice}")

print(item_list[choice])

if item_list[choice] == "rock":
    if random_choice == "rock":
        print("Draw")
    elif random_choice == "paper":
        print("You lose")
    elif random_choice == "scissors":
        print("You win")
elif item_list[choice] == "paper":
    if random_choice == "rock":
        print("You win")
    elif random_choice == "paper":
        print("Draw")
    elif random_choice == "scissors":
        print("You lose")
elif item_list[choice] == "scissors":
    if random_choice == "rock":
        print("You lose")
    elif random_choice == "paper":
        print("You win")
    elif random_choice == "scissors":
        print("Draw")
else:
    print("You did not enter a valid option")
```

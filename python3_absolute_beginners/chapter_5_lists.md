# Sequences

Python supports negative indexing of sequences. First index is 0 while last element index is counted in reverse as -1, last but previous element with index -2 and so on.

## Using python help

```Python
#  list all methods available in str
dir(str)

# provides documentation for the method
help(str.upper)

# use __doc__ method on objects
print(str.upper.__doc__)

# Another method to get the documentation of an object
# Remember functions in python are also objects
import inspect
inspect.getdoc(str.upper)
```

## String

Strings are immutable.

```Python
# accessing characters in a sequence
planet = "Earth"
print(planet[0])
print(planet[-1]) # last element has index -1.

# upper, lowern trim
planet.upper()
planet.lower()
planet.strip() # trims leading and trailing spaces.

# substring using slicing
# Syntax: str[from_start_index:before_end_index:step]
# start_index optional. default is first character
# end_index is also optional, default is length of the sequence
print(planet[0:3:2]) # prints Er

# contains
print("Ear" in planet) # returns True
print("Ear" not in planet) # returns False

# string concatenation
print("foo" + "bar")

# multiply to generate repetition
print(planet * 3)

# split syntax: str.split(separator, max_splits)
fruits="Apple,Mango,Orange"
fruits_list = fruits.split(",")

# convert a string to list of characters, tuple
list(planet)
tuple(planet)

# list to string
str(fruits_list) # adds [] to the output string

# string length
len(planet)

# count individual characters in a string
fruits.count("e")

# string comparison
"foo" > "bar"
"hello" < "world"
"moon" == "moon"

# empty string evaluates to false
empty_string=""
if not empty_string:
  print("Empty string evaluates to false in python")

if len(empty_string) == 0:
  print("Empty string")
```

## Tuple

Tuples are immutable. Can be used in methods to return multiple items

```Python
empty_tuple = ()
single_item_tuple = ("item1", ) # last comma is mandatory
l4_tuples = ("srcip", "destip", "srcport", "destport", "protocol")

# index accessing works
print(l4_tuples[0])

# length of tuple
len(l4_tuples)

# contains
print("srcport" in l4_tuples)

# slicing
l4_tuples[::2]

# count an item in the tuple
l4_tuples.count("destip")

# to string, list
str(l4_tuples)
list(l4_tuples)

# concat tuples
("10.10.10.10", "192.168.10.10") + ("12345", "80", "T")

# compare tuples
("10.10.10.10", "192.168.10.10", "12345", "80", "T") == ("10.10.10.10", "192.168.10.10", "12345", "80", "T")

# join tuple values
"_".join(l4_tuples) # prints 'srcip_destip_srcport_destport_protocol'
```

## List

Lists are mutable.

```Python
devices = ["monitor", "keyboard", "mouse", "printer"]

# empty list evaulates to false

# accessing a list element
print(devices[1])

# update list element
devices[2] = "wireless mouse"

# slicing a list
print(devices[::2])

# length of list
print(len(devices))

# adding element to the list
devices.append("cpu")

# concatenating another list to this list
devices.extend(["webcam", "speakers"])

# concat two lists to create a new list
computer_devices = devices + ["webcam", "speakers"]

# join list elements to a string
",".join(devices)

# list to string
str(devices)

# delete elements in a list
del devices[4:]

# index of a list element
devices.index("keyboard")

# insert at index
devices.insert(1, "joystick")

# remove first occurance of a particular element
devices.remove("printer")

# count, max, min
devices.count("monitor")

# remove and return a list element
# when no index is specified, defaults to the last element in the list
devices.pop(4)
```

## Stack and queues

```Python
# stack - Last In First Out
stack = []
stack.append("Item1") # added to last
stack.pop() # popped from last

# queues - First In First Out
queue = []
queue.append("item1") # add to last
queue.pop(0) # pop from front

```

## Sorting lists

```Python
# inplace sorting
numbers = [2, 4, 5, 1, 3]
numbers.sort()

# numerical arrays can use builtins max and min
min(numbers)
max(numbers)

# new list without modifying existing list
sorted(numbers)

# inplace sorting
numbers.sort()

# reversing list inplace
numbers.reverse()

# reverse to new list
reversed(numbers) # returns an iterator
```

## Multidimensional lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

## Iterating through lists

```Python
numbers = [2, 4, 5, 1, 3]

# iterating through a list
for el in numbers:
  print(el)

# using enumerate builtin
for pos, value in enumerate(numbers):
  print(pos, value)

# looping through two lists simultaneously
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
for e1, e2 in zip(list1, list2)
  print(e1, e2)
```

## List comprehensions

Syntax: **[expression for var in list [for ... | if ...]]**

**NOTE**: Scope of loop variable is within the list comprehension. The loop variables will not be available outside the list comprehension.

```Python
fruits = ["apple", "orange", "mango", "banana"]
# scope of fruit is within []
[fruit.upper() for fruit in fruits]
```

* Multiple levels of `for` can follow one another

```Python
# Print all two tuples such that i+j != 5
[(i, j) for i in range(0, 10) for j in range(0, 10) if (i + j != 5)]
```

## Set

All elements in a list are unique. Elements cannot be accessed through index in a set.

```Python
empty_set = set()

# set from list
fruits1 = ["apple", "mango", "orange", "mango", "banana"]
fruits_set1 = set(fruits1)

# direct set initialization
fruits_set = {"avacado", "watermelon", "pieapple", "muskmelon"}

# set difference a - b -> returns elements only found in a
fruits_set1 - fruits_set2
fruits_set2 - fruits_set1

# intersection
fruits_set1 | fruits_set2

# union
fruits_set1 & fruits_set2

```

## Dictionary

Key must be of immutable type integer, float, string, tuple

```Python
empty_dict = {}

details = {"name": "John Doe", "age": 25, "mobile": "123456789", "gender": "male"}

print(details["name"])

# iterate through dictionary
for key in details:
  print("Key:" + key + ", value:" + str(details[key]))

if "name" in details:
  print(details["name"])
else:
  print("name entry not available")

# get a default value from dictionary when key is not present
gender = details.get("gender", "NotPresent")

keys_list = details.keys()
values_list = details.values()
key_value_pairs = details.items()

for key, value in details.items():
  print(",".join([key, value]))

# length of the dictionary
len(details)

# blank dictionary from list
fruits = ["Apple", "Mango", "Orange"]
# values are set to None
dict.fromkeys(fruits)

# deleting items from dictionary
del details["gender"]

# fetch the value and the delete
age = details.pop("age", -1)

# popitem() returns a random key value tuple.
# on empty dictionary, KeyError is raised
key_value = details.popitem()

# clear all items in a dictionary
details.clear()

# sorting dictionary items
sorted(details.items())
```

### `defaultdict`

The default factory is called without arguments to produce
a new value when a key is not present, in `__getitem__` only.

```Python
from collections import defaultdict

# default_factory should be a callable that works with no parameters
# if we have a callable with parameters then we can wrap that callable
# in a lambda expression or using functools.partial
empty_map = defaultdict(int)
len(empty_map)
# This should insert 0 against some_key and return the value 0
empty_map["some_key"]
len(empty_map) # should be 1
```

---

## References

* [Python course](https://www.python-course.eu/python3_dictionaries.php)
* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)

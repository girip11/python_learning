# Enumeration in python

> An enumeration is a set of symbolic names (members) bound to unique, constant values. Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over.

## Defining enumeration

### Subclassing

* Every enum is defined as an attribute of a type inheriting from `Enum`

```Python
from enum import Enum

# though subclassing
class Animals(Enum):
    CAT = 1
    DOG = 2
    HORSE = 3

print(isinstance(Animals.CAT, Animals))
```

* Enumerations are Python classes, and can have methods and special methods as usual.

* Also we can assign any arbitrary value to the enumeration members(not only `int`).

### Functional way

```Python
# using Enum class itself
AnimalsEnum = Enum("Animals", ["CAT", "DOG", "HORSE"], start=1)
```

* Automatically assigning values using `enum.auto`

```Python
from enum import auto

class Animals(Enum):
    CAT = auto()
    DOG = auto()
    HORSE = auto()
```

## Iterating over enums

* Enums are iterable.

* Each field in the enumeration is an object has `name` and `value`

```Python
for animal in Animals:
    print(type(animal))
    print(animal.name, animal.value)

# we can get the enum object using the value as well as the name
animal_from_value = Animals(2)

# case matters
animal_from_name = Animals["DOG"]

print(animal_from_name is animal_from_value)
```

* Enum objects are compared based on their identity.

## Extras on `Enum`

* Ensuring unique values for enumerations using `enum.unique` decorator. Without this decorator, multiple members can have same values.

```Python
from enum import unique, Enum, DuplicateFreeEnum

# This definition will raise ValueError
@unique
class Animals(Enum):
    A = 1
    B = 1 
```

* Enumeration members are hashable, so they can be used as keys in dictionary.

* `Enum.__members__` is a dictionary of member name to the member enum object.

* Subclassing an enumeration is allowed only if the enumeration does not define any enum members.

* Enumerations can be pickled and unpickled.

* [Examples from python docs](https://docs.python.org/3.4/library/enum.html#interesting-examples)

---

## References

* [Python enumeration](https://docs.python.org/3/library/enum.html)
* [Intro into enumeration](https://dzone.com/articles/python-3-an-intro-to-enumerations)

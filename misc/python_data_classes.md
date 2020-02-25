# Data classes in Python 3.7

* Data classes come with default `__init__()`, `__repr__()` and `__eq__()`.

* **Same as regular class** but with less boilerplate code

* Type hinting **mandatory**. If the type is not known `Any` can be used.

* Methods can be added to the dataclasses.

* `help(dataclasses.dataclass)` - documentation

```Python
class SimpleClass:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"""{{
            "name": "{self.name}",
            "age": {self.age}
        }}
        """

sc = SimpleDataClass('John', 50)
print(sc)

from dataclasses import dataclass

@dataclass
class SimpleDataClass:
    # With default values
    name: str = ""
    age: int = 25

# Attributes with default value can be omitted while instantiation.
sd = SimpleDataClass('Jane')
# Output: SimpleDataClass(name='Jane', age=25)
print(sd)

sd2 = SimpleDataClass('Jane')
print(sd == sd2)    # True
print(sc == sd)     # False
```

## Named Tuple vs Dataclasses

* Named tuple is immutable
* Named tuple can be compared against another named tuple which could lead to subtle bugs

## Defining dataclass similar to named tuple

* `help(dataclass.make_dataclass)` - documentation on the method

```Python
from collections import namedtuple
Student = namedtuple("Student", ["Name", "Age"])

from dataclasses import make_dataclass
Employee = make_dataclass("Employee", ["Name", "Age"])
```

## Immutable dataclasses

* Immutable - Only the variable reference to the underlying object cannot be changed, but the state of the object itself can be changed.

```Python
from dataclasses import make_dataclass, dataclass

@dataclass(frozen = True)
class Employee:
    name: str
    age: int

Employee = make_dataclass("Employee", [("Name", str), ("Age", int)], frozen= True)
```

## Inheritance

* During instantiation, parameters will follow the inheritance order, starting from the attributes of the base class to derived class.

> If a field in a base class has a default value, then all new fields added in a subclass must have default values as well.
> Another thing to be aware of is how fields are ordered in a subclass. Starting with the base class, fields are ordered in the order in which they are first defined. If a field is redefined in a subclass, its order does not change.

## Optimization

* [**slots**](slots_in_python.md) can be used to optimize dataclasses to consume less memory and less cpu time

---

## References

* [The Ultimate Guide to Data Classes in Python 3.7](https://realpython.com/python-data-classes/)

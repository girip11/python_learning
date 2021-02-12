# Data classes in Python 3.7

* Data classes come with default `__init__()`, `__repr__()` and `__eq__()` (i.e) **Same as regular class** but with less boilerplate code

* Type hinting **mandatory**. If the type is not known `Any` can be used. But even if you pass an object of someother type in the runtime, it would still work since python being dynamically typed.

* These type annotations can be used by static type checkers like **mypy**

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

from dataclasses import dataclass, is_dataclass

@dataclass
class SimpleDataClass:
    # With default values
    name: str = ""
    age: int = 25

# Attributes with default value can be omitted while instantiation.
sd = SimpleDataClass('Jane')
# Output: SimpleDataClass(name='Jane', age=25)
print(sd)

# Helps to check if this instance in that of a dataclass
# The same also works on a class as well
print(is_dataclass(SimpleDataClass))
print(is_dataclass(sd))


sd2 = SimpleDataClass('Jane')
print(sd == sd2)    # True
print(sc == sd)     # False
```

* To the dataclass decorator, we can pass parameters like `init`(default True), `repr`(default True), `order`(default False), `eq`(default True), `frozen`(default False), `unsafe_hash`(default False)(all these parameters accept boolean values) to add or remove relevant methods.

```Python
# dataclass decorator signature
@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
```

**NOTE**: Note that `eq` must be `True` if `order` is `True` otherwise `ValueError` exception will raise.

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

# With type annotations, default values and customizations.
AnotherEmployee = make_dataclass("Employee", [("name", str), ("age", int, 30)], frozen= True)
```

## Immutable dataclasses

* Immutable - Only the variable reference to the underlying object cannot be changed, but the state of the object itself can be changed.

```Python
from dataclasses import make_dataclass, dataclass

@dataclass(frozen = True)
class Employee:
    name: str
    age: int

employee = Employee(name = "John")
# This will raise error FrozenInstanceError
employee.age = 25
```

* When creating frozen instances with default values for some fields, we need to define a custom `__init__` method, to accept the values passed via the `__init__`method. Otherwise we cannot override the default values.

```Python
from dataclasses import dataclass, field

@dataclass(init= False, frozen= True)
class Employee:
    name: str
    age: int = 30

    def __init__(self, name, age):
        super().__setattr__("name", name)
        super().__setattr__("age", age)

# or we could use the dataclasses.field to set the default value
@dataclass(frozen=True)
class Employee:
    name: str
    age: int = field(default=30)

john = Employee("John", 25)
```

* If the parent dataclass is frozen, then the subclasses inheriting from that parent should also be frozen.

## Cloning from an existing dataclass object

```Python
from dataclasses import dataclass, replace

@dataclass
class Employee:
    name: str
    age: int

john = Employee(name="John", age=25)
jane = replace(john, name="Jane")
print(john)
print(jane)
```

## Post init processing

* Dataclasses can invoke `__post_init__` special method from the **generated** `__init__`.

* If we have set `__init__` to `False`, then `__init__` will not be generated and hence the `__post_init__` method will not be automatically called.

```Python
from dataclasses import dataclass, field, fields

@dataclass
class Person:
    first_name: str
    last_name: str
    # This will make the field not to be passed through
    # the __init__ method
    full_name: str = field(init=False)
    age: int

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"

john = Person("John", "Doe", 25)
print(john)

# This will return the tuple of Field of john
# excluding the fields that are annotated as ClassVar
# and InitVar
print(fields(john))
```

* `field` can accept parameters as in `dataclasses.field(*, default=MISSING, default_factory=MISSING, repr=True, hash=None, init=True, compare=True, metadata=None)`

## Comparing data classes

> By default, `order` parameter of data class is `False`. When you set it to `True`, `__lt__`, `__le__`,`__gt__` and `__ge__` methods will be automagically generated for your data class. So you can make comparison of objects as if they were tuples of their fields in order.

```Python
from dataclasses import dataclass, field

# Order is set to True, so that comparison will happen
# against the fields in the order that they are defined
@dataclass(order=True)
class Vector:
    # Comparison will be first made against magnitude
    # followed by x and then y
    magnitude: float = field(init=False)
    x: int
    y: int

def __post_init__(self):
    self.magnitude = (self.x ** 2 + self.y ** 2) ** 0.5

v1 = Vector(8, 15)
v2 = Vector(7, 20)
print(v2 > v1)
```

## Converting to `dict` and `tuple`

```Python
from dataclasses import asdict, astuple, dataclass

@dataclass
class Employee:
    name: str
    age: int

john = Employee(name="John", age=25)
print(asdict(john))
# tuple will contain only the values
print(astuple(john))
```

## Class variables and init only variables

* To declare class only variable, we can use the `typing.ClassVar` annotation.

* Variables annotated with `dataclasses.InitVar` are considered to be an init only field. Init only fields are added as parameters to the `__init__` as well as passed to the optional `__post_init__` methods.

* To the `__post_init__` method, the init only fields are passed in the order in which they are declared in the class.

* Init only fields are not returned by the `dataclasses.fields` function.

```Python
@dataclass
class C:
    i: int
    j: int = None
    database: InitVar[DatabaseType] = None

    # the init var is used to initialize some of the dataclass
    # fields that were not initialized during the instance creation.
    def __post_init__(self, database):
        if self.j is None and database is not None:
            self.j = database.lookup('j')

c = C(i = 10, database=my_database)
```

## Inheritance

* Dataclasses can be subclassed like normal classes in Python.

* During instantiation, parameters will follow the inheritance order, starting from the attributes of the base class to derived class.

> If a field in a base class has a default value, then all new fields added in a subclass must have default values as well.

* Above can be overcome if we use `field` to assign default values.

```Python
from dataclasses import *
from typing import *

@dataclass(frozen=True)
class Person:
    count: ClassVar[int] = 0
    first_name: str
    last_name: str
    age: int
    full_name: int = field(default="", init=False)
    vehicle: InitVar[str]
    owns_vehicle: bool = field(default=False, init=False)
    def __post_init__(self, vehicle):
        super().__setattr__("full_name",f"{self.first_name} {self.last_name}")
        super().__setattr__("owns_vehicle",  vehicle is not None)


@dataclass(frozen=True)
class Student(Person):
    course: str

s = Student(first_name="John", last_name="Doe", age=20, vehicle="Honda Civic", course="computer")

vars(s)
```

> Another thing to be aware of is how fields are ordered in a subclass. Starting with the base class, fields are ordered in the order in which they are first defined. If a field is redefined in a subclass, its order does not change.

## Optimization

* [**slots**](slots_in_python.md) can be used to optimize dataclasses to consume less memory and less cpu time.

```Python
from dataclasses import dataclass

@dataclass
class Employee:
    __slots__ = ('name', 'age')
    name: str
    age: int

John = Employee('John', 25)
```

---

## References

* [The Ultimate Guide to Data Classes in Python 3.7](https://realpython.com/python-data-classes/)
* [Dataclasses in Python](https://medium.com/mindorks/understanding-python-dataclasses-part-1-c3ccd4355c34)
* [Dataclasses in python: towardsdatascience](https://towardsdatascience.com/data-classes-in-python-8d1a09c1294b)

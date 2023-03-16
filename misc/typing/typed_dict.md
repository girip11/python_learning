# Python TypedDict (3.8)

- TypedDict -> Type Hints for Dictionaries with a **Fixed Set of Keys**
- TypedDict is a simple typed namespace. At runtime it is equivalent to a plain `dict`.

> Support the use case where a dictionary object has a **specific set of string keys, each with a value of a specific type**. - PEP 589

- If using python < 3.8, we need to install the **mypy_extensions** package to access the `TypedDict`.

```Python
# Before Python 3.8
from mypy_extensions import TypedDict

# From python 3.8
from typing import TypedDict
```

- TypedDict types can't be used in `isinstance()` or `issubclass()` checks.

## Basic Usage

```Python
from typing import TypedDict

# name and profession are the keys that will be present
# in this person dictionary
# Value held by the name key will be a string
# Value held by the age key will
class Person(TypedDict):
    name: str
    age: int

john: Person = Person(name="John", age = 25)

john: Person = dict(name="John", age = 25)

john: Person = { name: "John", age: 25}
```

## TypedDict vs Dataclasses

- In a dataclass, we can either create a field that can be initialized during instance creation passing the parameter to the `__init__` method or initialize a field later by adding `field(init = False)` setting. During runtime we don't have the flexibility to include or exclude fields from passing to `__init__` method. We might have to pass some default values like `None` to those missing.

```Python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
  name: str
  age: int
  car: Optional[str] = None
  bike: Optional[str] = None
  bank: Optional[str] = None
  console: Optional[str] = None

larry = Person(name="Larry", age=25, car="Kia Spectra")
# Person(name='Larry', age=25, car='Kia Spectra', bike=None, bank=None, console=None)
print(larry)
```

- In cases where we have a lot of optional fields which can be either initialized during creation or later, in such cases `TypedDict` seem to provide more flexibility compared to dataclasses.

```Python
from typing import TypedDict
# By default, all keys must be present in a TypedDict.
# It is possible to override this by specifying totality.
# Not all keys need to be present when an instance is created
class _Person(TypedDict, total=False):
  car: str
  bike: str
  bank: str
  console: str

class Person(_Person):
  name: str
  age: int

larry: Person = dict(name="Larry", age=25, car="Kia Spectra")
# Person(name='Larry', age=25, car='Kia Spectra')
print(larry)
```

> We would recommend using TypedDict in situations where you're already using dicts. In these cases, TypedDict can add a degree of type safety without having to rewrite your code. For a new project, though, I'd recommend using dataclasses. It works better with Python's type system and will lead to more resilient code. - [TypedDict vs Dataclasses](https://meeshkan.com/blog/typedict-vs-dataclasses-in-python/)

## Typing hinting `**kwargs`

- Proposed [PEP 692](https://peps.python.org/pep-0692/)

```Python
from typing import TypedDict
from typing_extensions import Unpack #mypy

class Movie(TypedDict):
    name: str
    year: int

def foo(**kwargs: Unpack[Movie]) -> None: ...
```

---

## References

- [Python TypedDict](https://mpkocher.github.io/2019/09/19/Exploring-TypedDict-in-Python-3-8/)

- [PEP:589 TypedDict](https://www.python.org/dev/peps/pep-0589/)

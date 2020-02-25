# Type hinting in python (From Python 3.6 onwards)

* Use **Mypy** package and its corresponding extension in vscode.

* Type hints are ignored during runtime by the python interpreter.
* Helpful for static type checking.
* For better type hinting support use **python 3.8** and above

## Builtin simple types

* `int`, `bool`, `float`, `str`, `bytes`

```Python
b: bytes = b"hello"
```

* With typehints we can have plain declaration statements without assigning any value.

```Python
import random

def random_enable():
    # This is a declaration statement
    # This will be ignored by the python interpreter
    # Variable is created during its first assignment.
    # The same can be verified using the locals()
    print(f"Start of the function: {locals()}")

    # You don't need to initialize a variable to annotate it
    enabled: bool
    print(f"After the type hint statement: {locals()}")
    if random.choice(range(1, 10)) >= 5:
        enabled = True
    else:
        enabled = False
    print(f"End of the function: {locals()}")

    return enabled

print(f"Enabled: {random_enable()}")
```

## `typing` module

```Python
from typing import List, Set, Dict, Tuple, Optional, Union

roles: List[str]

# Role profile name and list of roles in that role profile
role_profiles: Dict[str, List[str]]

distinct_choices: Set[int]

two_tuple: Tuple[int, float] = (1, 100.0)

# Optional is used when the variable can also have None value
# assign_role can return a role name or None
# if no role needs to be assigned
role: Optional[str] = assign_role()

if role is not None:
    print(role)

# Union[x, y] - can be of type either x or y
email_recipients: Union[str, List[str]]

```

## Functions

* `None` is used as the return type for functions without return values

```Python
def say_hello(name: str) -> None:
    print(f"Hello, {name}")

say_hello("John")
```

* Function that returns an **iterator** uses `Iterator[type]`

```Python
from typing import Iterator

def find_common_letter_by_position(str1: str, str2: str) -> Iterator[str]:
    return (i for i,j in zip(str1, str2) if i == j)

for c in find_common_letter_by_position("abcdef", "abdyef"):
    print(c)
```

* Iterators can also be used as return value type from the generator functions

```Python
from typing import Iterator

def get_iterable(n) -> Iterator[int]:
    for i in range(n):
        yield i

for i in get_iterable(10):
    print(i)
```

* Function that return generator objects. `Generator[yield_type, send_type, return_type]` can be used as the return type of generator functions

```Python
from typing import Generator

def get_iterable_gen(n) -> Generator[int, None, int]:
    count: int = 0
    for i in range(n):
        yield i
        count += 1
    return count

gen: Generator[int, None, int] = get_iterable_gen(10)
for i in gen:
    print(i)

# To capture the return value along with generator values
# iterate through the generator like below snippet
# gen: Generator[int, None, int] = get_iterable_gen(10)
# try:
#     i = next(gen)
#     while True:
#        print(i)
#        i = next(gen)
# except StopIteration as e:
#     # return value from generator stored in value attribute
#     # of StopIteration exception
#     print(e.value)
```

* `Callable[[param_type, ...], return_type]` is used in cases where a function can accept another function as argument, return a function or to annotate a variable storing a reference to the function object.

```Python
# Add default value for an argument after the type annotation
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float

# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f
```

## `Any` type and varargs

* `Any` used in places where the return value belongs to dynamic type

* If all `*args` or `**kwargs` are going to be of type `str`, we can use `str` to `*args` and `**kwargs`

```Python
from typing import Any

def simple_func(*args: str, **kwargs: str) -> None:
    pass

def simple_func_any(*args: Any, **kwargs: Any) -> None:
    pass
```

## Duck typing and Collections

* `Iterable[Type]` - can capture any iterable. **Iterable protocol** refers to implementing special method  `__iter__()`
* `Sequence[Type]` - any sequence that requires `len` and `__getitem__`(access through []). **Sequence protocol** refers to objects that have `__len__` and `__getitem__` special methods implemented.

```Python
from typing import Iterable, Sequence, List

def square(values: Iterable[int]) -> List[int]:
    return [i ** 2  for i in values]

square(range(1, 10))
```

* `Set[Type]` and `MutableSet[Type]` are available for read only and mutable sets.

* `Mapping[K, V]` - `dict` like object with `__getitem__` that is immutable.
* `MutableMapping[K, V]` - `dict` like object with `__getitem__` that is mutable.

```Python
from typing import MutableMapping, Mapping, Dict, List

def get_items_with_claims(claims_list: Mapping[str, List[str]], claim_count = 2) -> Iterable[str]:
    """
        If the claims_list is altered inside this function, static type analysis will raise error
    """
    return (k for k, v in claims_list.items() if len(v) >= claim_count)

def add_claims(claims_list: MutableMapping[str, List[str]], claims: Iterable[str]) -> None:
    """
    Since the mapping is mutable, the dict like mapping can
    be altered within the function
    """
    for entry in claim_entries:
        id, claim =  entry.split(",")

        if id in claims_list:
            claims_list[id].append(claim)
        else:
            claims_list[id] = list(claim)

input = {
    "A" : [],
    "B" : []
}
add_claims(input, ["A,a", "A,b", "B,b"])
```

## Classes and Custom types

```Python
from typing import List, Optional, ClassVar

class SimpleClass:
    # instance variables with default values
    instance_id: Optional[str] = 0

    # class variables
    instance_count: ClassVar[int] = 0

    # None for return type from dunder init method
    # No types applied for self parameter
    def __init__(self, name: str) -> None:
        self.name = name
        # type while initializing instance variable
        self.name_len: int = len(name)
        self.instance_id = id(self)
        SimpleClass.instance_count += 1

# Custom types can be used as it is
simple_class1: SimpleClass = SimpleClass("Jack")
simple_classes: List[SimpleClass] = [simple_class1]
```

---

## References

* [Support for type hints](https://docs.python.org/3/library/typing.html)
* [Mypy Python type hints cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
* [The state of type hints in Python](https://www.bernat.tech/the-state-of-type-hints-in-python/)

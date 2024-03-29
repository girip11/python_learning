# Type hinting in python (From Python 3.6 onwards)

- Use **Mypy** package and its corresponding extension in vscode.

- Type hints are ignored during runtime by the python interpreter.
- Helpful for static type checking.
- For better type hinting support use **python 3.8** and above

- Type annotations can be accessed using the **`__annotations__`** attribute

```Python
def say_hello(name: str) -> str:
    return f"Hello, {name}"

print(say_hello.__annotations__)
```

## Builtin simple types

- `int`, `bool`, `float`, `str`, `bytes`

```Python
b: bytes = b"hello"
```

- With typehints we can have plain declaration statements without assigning any value.

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

- To specify a **variable-length tuple of homogeneous type**, use literal ellipsis, e.g. `Tuple[int, ...]`. A plain Tuple is equivalent to `Tuple[Any, ...]`.

```Python
from typing import Tuple

coordinates: Tuple[int, ...]
coordinates = tuple((1, 2))
```

**NOTE**: `None` as a type hint is a special case and is replaced by `type(None)`

- `typing.Literal` - This type indicates the variable takes one of the specified literal values. Values passed to `Literal` should be of immutable type. This was introduced from python 3.8 onwards.

```Python
MODE = Literal["r", "rb", "w", "wb"]
def open_helper(file: str, mode: MODE) -> str:
    pass
```

## typing alias

- Type hints can be assigned to an alias and that alias can be used inplace of the types. Helps in simplying complex signatures.

`typing.TypeAlias` - introduced in python 3.10.

```Python
from typing import Dict, List, Tuple, TypeAlias

# Vector is an alias of List containing strings
Vector: TypeAlias = List[str]

def transform(names: Vector) -> Vector:
    pass

# Assume a map that contains house coordinates as the key and the
# visited count as the value. Instead of writing Dict[Tuple[int, int], int]
# using aliases we can make the signature more readable.
HouseCoordinates = Tuple[int, int]
VisitedHouses = Dict[HouseCoordinates, int]
```

## `NewType`

- Helps declaring subtypes of a type.

- This new type in runtime becomes a function that returns the passed value as it is to the caller. **Since this derived type is a function, we cannot create classes that inherit from this derived type**.

```Python
from typing import NewType, Tuple

# Remember Coordinates is not an alias of Tuple[int, int]
# Coordinates now becomes a subtype of Tuple[int, int]
Coordinates = NewType('Coordinates', Tuple[int, int])

# prints function
print(type(Coordinates))

# below will raise runtime ERROR
# since we cannot create class inheriting from function
class HouseCoordinates(Coordinates):
    pass

# we can create subtype from Coordinates using NewType
# this will define a function with name HospitalCoordinates in
# that module scope
HospitalCoordinates = NewType('HospitalCoordinates', Coordinates)
```

## Built-in collections from `typing` module

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

# optional can be written as Union[X, None] or X | None
role: str | None = assign_role()

if role is not None:
    print(role)

# Union[x, y] - can be of type either x or y
# Union comparision ignores the type order
email_recipients: Union[str, List[str]]

# Union can be written as X | Y from  python 3.10
email_recipients: str | List[str]
```

## Functions

### Simple functions

- `None` is used as the return type for functions without return values

```Python
def say_hello(name: str) -> None:
    print(f"Hello, {name}")

say_hello("John")
```

### Functions using iterators

- Function that returns an **iterator** uses `Iterator[type]`

```Python
from typing import Iterator

def find_common_letter_by_position(str1: str, str2: str) -> Iterator[str]:
    return (i for i,j in zip(str1, str2) if i == j)

for c in find_common_letter_by_position("abcdef", "abdyef"):
    print(c)
```

- Iterators can also be used as return value type from the generator functions

```Python
from typing import Iterator

def get_iterable(n) -> Iterator[int]:
    for i in range(n):
        yield i

for i in get_iterable(10):
    print(i)
```

### Generator functions

- Function that return generator objects. `Generator[yield_type, send_type, return_type]` can be used as the return type of generator functions

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

### Functions accepting or returning functions (Higher order functions)

- `Callable[[param_type, ...], return_type]` is used in cases where a function can accept another function as argument, return a function or to annotate a variable storing a reference to the function object.

```Python
# Add default value for an argument after the type annotation
def f(num1: int, my_float: float = 3.5) -> float:
    return num1 + my_float

# This is how you annotate a callable (function) value
x: Callable[[int, float], float] = f
```

- Parameters can be skipped using **literal ellipsis**(`...`). Ex: `Callable[..., int]`. Helpful in functions accepting just `*args` and `**kwargs`

### `Any` type and varargs

- `Any` used in places where the return value belongs to dynamic type.

> Any other type behaves as if it is a subtype of `Any`, and `Any` behaves as if it is a subtype of any other type.

- This behaviour of `Any` allows for **gradual typing** of python code. Say there is no type annotations, implicitly everything could be treated as `Any`.

> Consistent Types - The type T is consistent with the type U if T is a subtype of U or either T or U is `Any`.
> Formally, we say that a type T is a subtype of U if the following two conditions hold:
>
> - Every value from T is also in the set of values of U type.
> - Every function from U type is also in the set of functions of T type.

- With `Any`, any type checker would check for inconsistency in the typing.

- If all `*args` or `**kwargs` are going to be of type `str`, we can use `str` to `*args` and `**kwargs`

```Python
from typing import Any

def simple_func(*args: str, **kwargs: str) -> None:
    pass

def simple_func_any(*args: Any, **kwargs: Any) -> None:
    pass
```

**NOTE**: Use `object` to indicate that a value could be **any type in a typesafe manner**. Use `Any` to indicate that a value is **dynamically typed**.

## `AnyStr` type

- Its a constrained type. `AnyStr = TypeVar("AnyStr", str, bytes)`
- The argument passed to the parameter can be either str or bytes.

## Type Annotations

- When we want to add metadata to the variable alongside type hints, we can use `typing. Annotated`. Available from python 3.9 onwards.

> A type `T` can be annotated with metadata `x` via the typehint `Annotated[T, x]`. This metadata can be used for either static analysis or at runtime.

- Annotations must be called with **atleast two arguments**but have can many(vardiac)

```python
from typing import Annotated

def get_pitch_area(x: Annotated[float, "meters"], y: Annotated[float, "meters"]) -> Annotated[float, "square meters"]:
    ...

```

## Duck typing and Collections

- `Iterable[Type]` - can capture any iterable. **Iterable protocol** refers to implementing special method `__iter__()`
- `Sequence[Type]` - any sequence that requires `len` and `__getitem__`(access through []). **Sequence protocol** refers to objects that have `__len__` and `__getitem__` special methods implemented.

```Python
from typing import Iterable, Sequence, List

def square(values: Iterable[int]) -> List[int]:
    return [i ** 2  for i in values]

square(range(1, 10))
```

- `Set[Type]` and `MutableSet[Type]` are available for read only and mutable sets.

- `Mapping[K, V]` - `dict` like object with `__getitem__` that is immutable.
- `MutableMapping[K, V]` - `dict` like object with `__getitem__` that is mutable. Mapping covers `dict`, `UserDict`, `OrderedDict`, `ChainMap`, `defaultdict`.

- The `MutableMapping` class accepts any instance that implements the following special methods `__getitem__`, `__setitem__`, `__delitem__`, `__iter__`, `__len__`. `Mapping` accepts objects implementing `__getitem__`, `__iter__`, `__len__`

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

## TypedDict

- This is useful where the keys of the dictionary (keys must be strings) are known ahead. This helps to capture the value type of each key instead of typing as `Dict[str, Any]`

```python
from typing import TypedDict

# total=False so that all the keys are not required to be present in the dict
class EditorConfig(TypedDict, total=False):
    line_length: int
    placeholder_text: str
    wrap_text: bool

# we can pass this dictionary and type hint like this
def process_text(data: str, config: EditorConfig) -> None:
    ...

```

- `TypedDict` along with `Unpack` can be used to type hint the `**kwargs` in functions and methods. [PEP 692](https://peps.python.org/pep-0692/). This is experimental feature in mypy(`Unpack` has to be enabled)

```Python
# suppose we have function with keyword arguments
# If we know what are kwargs can be expected to be passed to this function
# we could use Unpack[TypedDict]
def read_csv(path: str, /, **kwargs) -> None:
    ...

from typing import TypedDict
from  typing_extensions import Unpack

class CSVOptions(TypedDict, total=False):
    sep: str
    header: bool

def read_csv(path: str, /, **kwargs: Unpack[CSVOptions]) -> None:
    ...
```

## Classes and Custom types

```Python
from typing import List, Optional, ClassVar

class SimpleClass:
    # instance variables with default values
    instance_id: Optional[str] = None

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

- `typing.overload` - Decorator to mark the methods as overloaded methods
  Remember in python method overloading is not allowed. This decorator helps overcome that.

> The @overload-decorated definitions are for the benefit of the type checker only, since they will be overwritten by the non-@overload-decorated definition, while the latter is used at runtime but should be ignored by a type checker. At runtime, calling a @overload-decorated function directly will raise `NotImplementedError` - **Python typing docs**

```Python
@overload
def process(response: str) -> None:
    pass

@overload
def process(response: int) -> Tuple[int, str]:
    pass

@overload
def process(response: bytes) -> str:
    pass

def process(response):
    <actual implementation>
```

- `typing.final` - decorator that can be used on classes or methods to indicate the type checker that the method cannot be overridden or the class cannot be subclassed.

- From python 3.8, `typing.Final` can be used to define constants from a static type check point.

```Python
from typing import Final
VERSION: Final = "1.0.0"
```

- `typing.type_check_only` - Decorator that makes a type available only during the type checking and unavailable during runtime.

- `typing.TYPE_CHECKING` - A special constant that is assumed to be True by 3rd party static type checkers. It is False at runtime.

## Forward references and casting

- `typing.cast(type, value)` - to cast value to type. Used by static type checkers only. No runtime impact.

- `List["SomeClass"]` syntax can be used to refer to forward references and will be implicitly transformed to `List[ForwardRef("SomeClass")]` by the static type checking tools.

- Another way to handle forward references is to use `__future__.annotations`. Python 3.7 and above this is available.

```Python
from __future__ import annotations

class Deck:
    @classmethod
    def create(cls, shuffle: bool = False) -> Deck:
        ...
```

Reason why we might not need to use forward references when importing `from __future__ import annotations` is

> Note If `from __future__ import annotations` is used in Python 3.7 or later, **annotations are not evaluated at function definition time**. Instead, they are stored as strings in `__annotations__`, This makes it unnecessary to use quotes around the annotation.

---

## References

- [Support for type hints](https://docs.python.org/3/library/typing.html)
- [Mypy Python type hints cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
- [Python type hinting guide](https://realpython.com/python-type-checking/)
- [The state of type hints in Python](https://www.bernat.tech/the-state-of-type-hints-in-python/)

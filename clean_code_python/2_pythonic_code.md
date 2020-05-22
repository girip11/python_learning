# Pythonic code

## Indices and slices

* Python does not offer head/first and tail/last methods like in other programming languages(Remember **There should be one-- and preferably only one --obvious way to do it.** from the Zen of Python)

* In python we can access elements using the negative indices. Negative index -1 points to the last element in the array. This is considered more pythonic than `mylist[len(mylist) - 1]`

```Python
mylist = [1, 2, 3, 4, 5]

# Accessing the first element
print(mylist[0])

# Accessing the last element in the list
print(mylist[-1])
```

* Slice should be preferred when a subset of list/tuple is required.

* Slice syntax `mylist[start:end:step]`. This will select all the elements starting from index start till the index end(excluding end) with selecting every step element in between.

* By default start is 0 and end is equal to length of the list.

* Default step value is 1.

```Python
mylist = [1, 2, 3, 4, 5]
# start index : stop index: step
sliced_list = mylist[1:4:2]

print(sliced_list)

# subset starting from index 1 till the end of the list
print(mylist[1:])

# makes a copy of the list.
print(mylist[::])
```

* The above is a **syntactic sugar** for the slice object. `help(slice)` for more details on slice. It is recommended to use the `::` syntax for slicing.

```Python
mylist = [1, 2, 3, 4, 5]
interval = slice(1,4,2)

print(mylist[interval])

print(mylist[slice(1, None)])

print(mylist[slice(None, 3)])
```

## Creating custom sequences

* In python, when an object is accessed like `myobject[key]`, magic method `__getitem__` is invoked on that object.

* Sequence in python should implement `__getitem__` and `__len__` methods.

* Sequences can be used in the `for .. in` loop.

* In the `__getitem__`, when the key is not found in the sequence, we need to raise `IndexError`. This error will be used by `for..in` loop as the terminating condition. No other exception is recognized as the terminating condition of the sequence iteration by the `for..in` loop.

* Approaches to create custom sequences
  * Wrapper over sequences from standard library
  * Inheriting sequences from standard library
  * Complete custom implementation
    * Slice should return an instance of the same type of the class
    * slice semantics should be preserved(excluding the last element)

## Context Managers

* Whenever we need to run a piece of code that has preconditions and postconditions to be run, we can use context managers to achieve this.

* Context managers are often used for resource management like file, database connections etc.

```Python
with open('test.csv') as test_file:
    print(test_file.read())
```

* Context managers contain `__enter__` and `__exit__` magic methods. Context managers are used in `with` statement in python.

* The return value of the  `__enter__(self)` method can be captured in a variable using the `as` keyword. Capturing the return value in a variable is optional and only needed when we want to do some operations on the object returned.

* It is a good practice to always return something from `__enter__`. When we don't have anything useful to return we can return the context manager object itself.

* `__exit__(self, ex_type, ex_value, ex_traceback)` is the signature of the exit method. In case an exception was raised inside the context manager block, this method will be called with the details of the exception, so that we can handle in a custom fashion, but the exception will still be passed on to the code following the `with` statement block.

* If we return `True` or any value that evaluates to `True` from `__exit__` method, the exception raised will be swallowed. **This is not considered a good practice**.

### Using `contextlib.contextmanager`

* When contextmanager decorator is applied to a function, the function should be a generator function.

```Python
from contextlib import contextmanager
@contextmanager
def some_generator(<arguments>):
    <setup>
    try:
        yield <value>
    finally:
        <cleanup>

with some_generator(<arguments>) as <variable>:
    <body>
```

* When we just need a context manager function, without preserving many states, and completely isolated and independent from the rest of our classes, this is probably a good way to go.

```Python
import contextlib

@contextlib.contextmanager
def contextmgr():
    print("This is where your precondition logic goes")
    # Anything yielded can be captured using the "as"
    yield "Say Hello"
    print("This is where your postcondition logic goes")

# msg contains "Say Hello"
with contextmgr() as msg:
    print(f"Message from context manager: {msg}")
```

### Using `contextlib.ContextDecorator`

* Mixin approach where `contextlib.ContextDecorator` is the mixin base class.

```Python
import contextlib

class ContextManager(contextlib.ContextDecorator):
    def __enter__(self):
        print("Execute precondition logic")

    def __exit__(self, ex_type, ex_value, ex_traceback):
        print("Execute postcondition logic")

@ContextManager()
def business_logic():
    print("business logic here")

# No with statement required. Calling the function is sufficient
business_logic()
```

* Advantage is we can use the decorator on any function that needs the same logic. Highly reusable.

* Drawback with this approach is that we cannot use the value returned by  the `__enter__` method as in `with contextmgr() as obj`.

### Suppressing particular exceptions

* This is one of the cases where returning `True` (any truthy value) from `__exit_` is exploited.

* `contextlib.suppress` can accept a list of exceptions and can handle those gracefully. This is equivalent to handling with `try..except` but with concisely.

```Python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove(somefile)
```

## Underscores in python

* All attributes(properties or functions) are public by default.

* Attributes prefixed with single underscore should be considered **private to that module/class by convention**.

* Identifiers with names prefixed with double underscores are subjected to name mangling. **This should only be used in inheritance case to avoid name collision. This should not be exploited to make an attribute private.**

## Properties

* Using the `@property` decorator is considered pythonic compared to getters and setters.

* Using properties we can define custom getter and setters to instance variables.

* Using properties we can adhere to **command query separation**.

```Python
from typing import Optional

class Student:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self._email: Optional[str] = None

    @property
    def email() -> str:
        return self._email

    @email.setter
    def email(email: str)-> None:
        if _isvalid(email):
            self._email = email
        else
            raise ValueError(f"{email} is not a valid email address")
```

## Iterable objects

* Python checks if the object used in the `for .. in` loop is an iterable or a sequence.

* An iterable follows iteration protocol in python. Iteration protocol requires objects to implement `__iter__` and `__next__` magic methods.

* `iter()` method is called on the objects used in the loop which inturn invokes the `__iter__` magic method. If the `__iter__` magic method is not found, then `iter()` looks for `__getitem__`.

* On the return value of the `__iter__` method, `next()` is called for every iteration.

```Python
import random
class RandomRange:
    def __init__(self) -> None:
        self._min = random.randint(1, 100)
        self._max = random.randint(self._min, 1000)
        self._current = self._min

    def __iter__(self)-> "RandomRange":
        return self

    def __next__(self) -> int:
        if self._current > self._max:
            raise StopIteration
        current = self._current
        self._current += 1
        return current

for i in RandomRange():
    print(i)
```

## Container Iterables

* When an iterable object is implemented similar to the above example, it can be iterated only once.

* To overcome this problem, an iterable object on calling `__iter__` method **constructs an iterator and returns it**. The iterable is referred to as the **container iterable**

* Iterators can be implemented using generator functions as well as separate classes with their own `__iter__` and `__next__` methods.

> In general, it is a good idea to work with container iterables when dealing with generators.

```Python
import random
from typing import Generator

class RandomRange:
    def __init__(self) -> None:
        self._min = random.randint(1, 100)
        self._max = random.randint(self._min, 200)

    # On every invocation of this method, it returns a generator
    # Generator is an iterator
    def __iter__(self)-> Generator:
        current = self._min
        while current < self._max:
            yield current
            current += 1

for i in RandomRange():
    print(i)
```

**NOTE**: [This article](https://python-patterns.guide/gang-of-four/iterator/#implementing-an-iterable-and-iterator) nicely explains the implementation of the container iterables and iterators.

## Iterable vs Sequence

* Iterables(container iterables) are memory efficient but cpu intensive. To reach the nth element, we have to iterate n times.
* Sequences are compute efficient but consume more memory. To fetch nth element it is O(1).

> Evaluate the trade-off between memory and CPU usage when deciding which one of the two possible implementations to use. In general, the iteration is preferable (and generators even more), but keep in mind the requirements of every case.

## Container Objects

* Implemented using the `__contains__` method. This is called when the object is used in the `in` expression of the form `element in container`.

```Python
from typing import Tuple
class Boundary:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def __contains__(self, coord: Tuple[int, int]) -> bool:
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height

class Grid:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._limits = Boundary(width, height)

    def __contains__(self, coord: Tuple[int, int]) -> bool:
        return coord in self._limits


# usage of in could make the code much more readable.
def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = MARKED
```

## Dynamic Attributes

* When an attribute on an object is invoked using the dot notation `myobject.attribute`, first `__getattribute__` magic method is called on that object. If the attribute is missing from that object dictionary `__dict__`, then the `__getattribute__` will fail. Then as a fallback `__getattr__` is called.

* `__getattr__` works for both fields and methods.

* `__getattr__` - we can control the access to dynamic attributes.

* `__getattr__` magic method should raise `AttributeError` when the attribute cannot be found by this magic method.

```Python
class DynamicAttributes:
    def __init__(self, attr):
        self.attr = attr

    def __getattr__(self, attr_name):
        if attr_name.startswith("fallback_"):
            name = attr_name.replace("fallback_", "")
            return self.__dict__[name]

        raise AttributeError(f"{self.__class__.__name__} does not have {attr_name}")

dyn = DynamicAttributes("Hello")
print(dyn.attr)

# This accesses via __getattr__
print(dyn.fallback_attr)

# This calls __getattr__ and when the magic method raises
# AttributeError default value is returned.
getattr(dyn, "name", "John")
```

## Callable Objects

* Objects can be invoked like functions. Applied in decorators.
* Objects should implement magic method `__call__` so that the object can be called like a function.

* Since **objects can maintain states**, mimicking function through objects help us retain the state across call (**functions with memory**).

> When we have an object, a statement like this `object(*args, **kwargs)` is translated in Python to `object.__call__(*args,**kwargs)`

```Python
from collections import defaultdict

class CallCounter:
    def __init__(self):
        self._counter = defaultdict(int)

    def __call__(self, argument):
        self._counter[argument] += 1
        return self._counter[argument]

counter = CallCounter()

print(counter(1))
print(counter(2))
print(counter(1))
```

## Caveats in Python

### Mutable default arguments

* Default value expressions are computed and the value of that expression is assigned to the function parameter exactly once.

* When the function is called everytime to use the default value, **same object** will be used as the value of the parameter.

```Python
def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"

wrong_user_display()
# raises error
wrong_user_display()
```

* Avoid mutable data structures as values for default arguments.

```Python
# Cleaner solution
def user_display(user_metadata: dict = None):
    user_metadata = user_metadata or {"name": "John", "age": 30}
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} ({age})"
```

### Extending builtin types

* Always use types in the `collections` module as the base for extending lists, dicts.

```Python
# Incorrect
class BadList(list):
    pass

# Correct way
from collections import UserList
class GoodList(UserList):
    pass
```

* `collections.UserString`, `collections.UserList`, `collections.UserDict` should be used for extending string, list and dict respectively.

---

## References

* [Clean code in python by Mariano Anaya](https://www.oreilly.com/library/view/clean-code-in/9781788835831/)

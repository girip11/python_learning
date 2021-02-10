# Context Manager in Python

## Why Context managers

* Context managers are extremely useful when we wanted to perform some clean up after a specific piece of code is executed.

* Context managers reduce the verbosity.

```Python
# opening and closing file using try .. finally
f = open("some_file.txt", w)
try:
    f.write("Hello world")
finally:
    f.close()

# using with statement
with open("some_file.txt", w) as f:
    f.write("Hello world")
```

## Context manager protocol

* Any object that has `__enter__` and `__exit__` methods implemented can be used in the `with` statement.

* When `with` statement gets executed, first the expression next to the `with` keyword is executed and on the resulting object of the expression `__enter__` method is called. Value returned from the `__enter__` method can be captured in a variable using `as` keyword.

```Python
# This will raise error since int objects dont have __enter__ method
with int(2):
    print("Hello world")

# file objects returned by open have __enter__ and __exit implemented
f = open("some_file.txt")
dir(f)

# threading.Lock() returns lock object that
# also adheres to context management protocol.
dir(threading.Lock())
```

* Even when the code block inside the `with` statement raises any exception, `__exit__` is still called.

## Simple Example

```Python
class Counter:
    def __init__(self):
        self.reset()

    def reset(self):
        self.value = 0

    def inc(self):
        self.value += 1

    def __enter__(self):
        return self

    def __exit__(self, ex_type, ex_val, ex_tb):
        self.reset()

c = Counter()
with c:
    for _ in range(1, 100):
        c.inc()
    print(c.value)

print(c.value)
```

## Using `contextlib`

### `contextlib.contextmanager`

* Here we create a generator and decorate it with `contextlib.contextmanager`

* This decorator returns a function which when called returns an instance of `contextlib._GeneratorContextManager`. This instance implements the context manager protocol.

```Python
# this is to demonstrate what's going on
from contextlib import contextmanager

def gen_for_context_mgr(*args):
    print("This will be executed when __enter__ is called.")
    yield args
    print("This will be executed when __exit__ is called")

wrapper_func = contextmanager(gen_for_context_mgr)
print(type(wrapper_func))

#cm_obj is an instance of contextlib._GeneratorContextManager
cm_obj = wrapper_func("hello")
print(type(cm_obj))
print(dir(cm_obj)) # contains __enter__ and __exit__ methods

with cm_obj as args:
    print(f"args passed: {args}")

# OUTPUT
# This will be executed when __enter__ is called.
# args passed: ('hello',)
# This will be executed when __exit__ is called
```

* When `__enter__` is called, the generated is executed up to the `yield` statement. Result of the `yield` statement can also be captured in a variable using `as`.

* When we leave the `with` block, `__exit__` is called which executes the statements in the generator following the `yield` statement.

**NOTE**: For generators to be used as context managers, they should have exactly a single `yield` statement.

```Python
# this is an example of contextmanager usage
from contextlib import contextmanager

@contextmanager
def file_context_manager(filename: str):
    f = None
    try:
        f = open(filename, "w")
        yield f
    finally:
        if f is not None:
            f.close()

with file_context_manager("somefile.txt") as f:
    f.write("hello world")
```

## Handling exceptions

* When exception is raised inside the `with` block, the exception type, exception object and the traceback as passed to the `__exit__` method.

* `__exit__` method can choose to handle or ignore the exception. If the `__exit__` method returns `True` that means the exception was handled by it.

* Any return value other than `True` causes the `with` statement to raise the exception.

## Exercise

```Python
with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
```

Write a context manager when used in the above snippet produces the output below

```text
hi!
    hello
        bonjour
hey
```

My Solution

```Python
class Indenter:
     def __init__(self, spaces=2):
         self._level = -1
         self._prefix = " " * spaces
 
     def print(self, msg: str):
         print(f"{self._level * self._prefix}{msg}")
 
     def __enter__(self):
         self._level += 1
         return self
 
     def __exit__(self, ex_type, ex_val, ex_tb):
         self._level -= 1
         # this will cause the with to raise the exception
         return None
```

Refactoring above `Indenter` to be generator based so as to use it with `contextlib.contextmanager`

```Python
from contextlib import contextmanager

@contextmanager
def create_indenter(spaces=4):
    yield Indenter(spaces)

# this class now becomes
class Indenter:
     def __init__(self, spaces):
         self._level = 0
         self._prefix = " " * spaces
 
     def print(self, msg: str):
         print(f"{self._level * self._prefix}{msg}")
 
     def __enter__(self):
         self._level += 1
 
     def __exit__(self, ex_type, ex_val, ex_tb):
         self._level -= 1
         # this means we are handling the exception here
         return True

# usage
with create_indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')
```

---

## References

* [Python documentation](https://docs.python.org/3/reference/datamodel.html#context-managers)
* [contextlib — Utilities for with-statement contexts](https://docs.python.org/3/library/contextlib.html)
* [Context Managers and the “with” Statement in Python](https://dbader.org/blog/python-context-managers-and-with-statement)
* [GFG python context manager](https://www.geeksforgeeks.org/context-manager-in-python/)
* [Handling exceptions with Context managers](https://book.pythontips.com/en/latest/context_managers.html#handling-exceptions)

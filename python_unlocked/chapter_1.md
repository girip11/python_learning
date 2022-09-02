# Objects in Depth

- Object's characteristics are identity, value and type

- `id()` - builtin function that returns the memory address of the object in CPython.

- Object's type using `obj.__class__` or `type(obj)`.
- For classes defined on the runtime(user defined classes), we can change the type of the objects by setting/updating the `__class__` attribute.

- An object can be made a callable by implementing `__call__` method. `builtins.callable` function can be used to test if an object is a callable. We could also check for a callable using below snippet.

```Python
from typing import Callable
isinstance(id, Callable)
```

## Methods

- Methods in a classes are functions but when invoked the instance is always passed as implicit first argument by the interpreter.
- When method of an object is captured in a variable, `method` class is instantiated with the instance stored in `__self__` and function stored in `__func__`.

```Python
class C:
    def f():
        print("Nothing")

c = C()
f = c.f
print(type(f)) # method
print(id(c) == id(f.__self__))

# invoking via the method object
f()
# or
f.__func__(__f.__self__)
```

- In a user defined class, a function with atleast one argument can be added as a method outside of the class definition.

```Python
class C:
    ...

def print_type(obj):
    print(type(obj))

# Added a method to the class in the runtime
C.type = print_type
c = C()
# this works
c.type()
```

## Metaclasses

- Class has metaclass and a class is an object of its metaclass
- When a class is called, its meta class method is invoked with the class as the implicit argument.

```Python
class Meta(type):
    def __call__(*args):
        print("Inside meta class call", args)

class C(metaclass=Meta):
    ...

# instantiating C will invoke the Meta.__call__ method
c = C() # Meta.__call__(C)

```

---

## References

- [Python unlocked](https://www.amazon.in/Python-Unlocked-Arun-Tigeraniya/dp/1785885995)

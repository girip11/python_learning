# Interfaces in python

* Informal interface - duck typing
* Formal interface - using Abstract base classes.

## `abc` module

* `abc.ABC` is a class whose metaclass is `abc.ABCMeta`. This can be verified with `type(abc.ABC)`

* If a class inherits from `abc.ABC` and does not define any abstract method/property, then the class can still be instantiated.

```Python
import abc

class SimpleClass(abc.ABC):
    def do(self):
        print("Hello")

sc = SimpleClass()
```

* Even if the abstract methods have implementation,  the subclasses have to provide overriding implementation for the subclass instantiation to be possible.

```Python
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def do_something(self):
        print("Inside the base class")

# This class B is also abstract since it does not provide
# implementation for all abstract methods on A
class B(A):
    pass

try:
    # raises TypeError
    b = B()
except TypeError:
    pass

class C(A):
    def do_something(self):
        print("Inside the subclass C")
        # But I can call the base class implementation
        super().do_something()

c = C()
c.do_something()
```

## Subclasses via inheritance

```Python
from abc import ABCMeta, ABC, abstractmethod

class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def do(self):
        pass


class Base(ABC):
    @abstractmethod
    def do(self):
        pass

# This cannot be instantiated
class InheritedConcrete(Base):
    pass

assert issubclass(InheritedConcrete, Base)

# methods of base class added to the subclass
assert "do" in dir(InheritedConcrete)

# inheritance hierarchy is also reflected in the MRO
print(InheritedConcrete.__mro__)
```

## Virtual subclasses

* `abc.ABCMeta` adds a `register(subclass)` method to all the classes which have `abc.ABCMeta` as their metaclass or `abc.ABC` as their base class.

```Python
from abc import ABCMeta, ABC, abstractmethod

class MyABC(metaclass=ABCMeta):
    @abstractmethod
    def do(self):
        pass


class Base(ABC):
    @abstractmethod
    def do(self):
        pass

class Concrete:
    pass

MyABC.register(Concrete)
Base.register(Concrete)

# Both should return True
assert issubclass(Concrete, MyABC)
assert issubclass(Concrete, Base)

# do method will not be inherited to Concrete
# since it is virtually subclassed via register
assert "do" not in dir(Concrete)

# Base class hierarchy does not show up on the MRO for virtual subclasses
print(Concrete.__mro__)
```

* The reason for registered subclasses to be referred to as **virtual subclasses** is that the subclass does not inherit from those abstract base classes directly.

* Virtual subclasses can be instantiated even though they don't override the abstract methods of their registered abstract base classes.

**NOTE**: Virtual subclasses pass the `issubclass()` check. But the methods in the base classes are not available/inherited by the subclass.

### Example of virtual subclasses

In python we consider an object to be an iterable if it satisfies any of the below two criteria

* `__iter__()` and `__next__()` methods
* `__getitem__()` and `__len__()` - These objecs are also known as Sequences.

In our code, we might define abstract base class that marks the `__iter__()` and `__next__()` as abstract and any concrete implementations of this ABC is considered as an iterable.

But through virtual subclassing, the objects that implement the `__getitem__` and `__len__` methods can also be made to be recognized as iterables.

## Customizing subclass check

* `ABCMeta` adds `__subclasshook__(subclass)` method to each of its classes.
* `__subclasshook__()` should be implemented as a class method.
* `issubclass()` builtin calls `ABCMeta.__subclasscheck__()`(if our base type uses ABCMeta as its metaclass) which inturn calls the `__subclasshook__` method.

**NOTE**: `__subclasshook__` is available only on classes whose metaclass is `ABCMeta`.

```Python
import abc

class ParserBase(abc.ABC):
    @classmethod
    def __subclasshook__(cls, C):
        # logic for checking if C subclass of cls
        pass
```

## `__subclasshook__` vs `register`

> You must be careful when you’re combining `.__subclasshook__()` with `.register()`, as `.__subclasshook__()` takes precedence over virtual subclass registration. To ensure that the registered virtual subclasses are taken into consideration, you must add `NotImplemented` to the `.__subclasshook__()` dunder method.

## Defining abstract properties, static methods and class methods

```Python
from abc import ABC, abstractmethod

class SomeClass(ABC):
    @abstractmethod
    def some_func(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @classmethod
    @abstractmethod
    def get_something(cls):
        pass

    @staticmethod
    @abstractmethod
    def some_util():
        pass
```

---

## References

* [abstract base classes](https://www.python-course.eu/python3_abstract_classes.php)
* [abc module](https://docs.python.org/3/library/abc.html)
* [Implementing an Interface in Python](https://realpython.com/python-interface/)

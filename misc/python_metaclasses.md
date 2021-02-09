# Metaclasses in Python

## Type of classes

In python3, all classes are instances of `type` class

```Python
class SimpleClass:
    pass

# type of an instance of SimpleClass is the class itself
type(SimpleClass())

# type of the class is the `type` metaclass.
type(SimpleClass)
type(str) # builtins are also of type `type`

type(type) # type itself is an instance of the type metaclass
```

## Functional way of creating new types

* We can create new classes using the `type` builtin. `help(type)`
provides us with the signature `type(name_or_obj, bases, dict)` that would create a new type.

* When `type()` builtin is passed an object, it returns the type of the object.

* When `type()` is passed name, bases and dict we get a new Class with its `__name__` set to name parameter, `__bases__` set to bases parameter and `__dict__` set to the values of dict parameter.

```Python
# by default all types inherit from object
# we dont need to specify explicitly
attrs = {
    "attr": 1,
    "attr_val": lambda x: x.attr
    }

# attr will be a class variable
# attr_val will be an instance method
SimpleClass = type("SimpleClass", (), attrs)
dir(SimpleClass)
sc = SimpleClass()
sc.attr
sc.attr_val()
```

## How the class instantiation works?

```Python
class SimpleClass:
    pass

sc = SimpleClass()
```

* In the above snippet, `SimpleClass()` invokes `type.__call__()` which inturn calls `__new__` class method and `__init__` instance method.

* By default `__new__` and `__init__` are obtained from the class hierarchy. By default every class inherits from `object` and `object` contains a `__new__` method that knows how to create an instance.

* We can override `__new__` and `__init__` methods in the class that we create to customize instance creation and initialization respectively.

```Python
# one use case of override __new__ is to cache already created instances
# Remember __init__ is always called on the instance returned by __new__
# so in this case, if we define __init__ method on SimpleClass,
# the same cached object will be initialized every time we call SimpleClass()
class SimpleClass:
    _singleton = None
    def __new__(cls):
        if cls._singleton is None:
            cls._singleton = object.__new__(cls)
            cls._singleton._initialize()

        return cls._singleton

    # default initialization
    def _initialize(self):
        # do some initialization
        pass

sc1 = SimpleClass()
sc2 = SimpleClass()

print(sc1 is sc2)
```

## Why custom metaclass?

* `type` is the metaclass of all classes. If we want to customize that way in which our custom class will be created, then we need to customize `__new__` on its type which is the `type` metaclass.
* But attributes(methods like `__new__`) on `type` cannot be customized.
* Hence we would need to define new type that would act as metaclass for the classes that we wanted to created.
* Basically we are saying, these new classes are instances of our newly defined metaclass instead of the builtin `type` metaclass.

```Python
# This example is to demonstrate the syntax of usage
class CustomMeta(type):
    def __new__(cls, name, bases, dict_):
        print("This will get executed when interpreter creates the user defined class.")
        # While creating we could do some customization.
        return super().__new__(cls, name, bases, dict_)

    def __init__(cls, name, bases, dict_):
        print("This will be called after metaclass __new__ method")
        # some customization logic
        cls.say_hello = lambda : print("Hello")

    def __call__(self, *args, **kwargs):
        print("This will be called every time we call a class that has this as its metaclass")
        return super().__call__(*args, **kwargs)

class SimpleClass(metaclass=CustomMeta):
    pass

# Every class with CustomMeta as its metaclass will have
# say_hello method available
dir(SimpleClass)
SimpleClass.say_hello()

# This will invoke the metaclass __call__ method
sc = SimpleClass()
```

> In the same way that a class functions as a template for the creation of objects, a metaclass functions as a template for the creation of classes. Metaclasses are sometimes referred to as class factories. - [Metaclasses](https://realpython.com/python-metaclasses/)

---

## References

* [Python Metaclasses](https://realpython.com/python-metaclasses/)

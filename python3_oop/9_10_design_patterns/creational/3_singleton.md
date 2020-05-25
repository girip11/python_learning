# Singleton pattern

Most of the times we can live without singletons.

**NOTE**: Global shared object pattern is preferred to singleton pattern in most cases.

## When Singleton is required

* When only one instance of a class is required.
* The data stored by the object needs to be accessed globally.
* Lazy initialization is desirable.

## Implementations

* Examples of classic singleton implementations can be found [here](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html)

* Singleton pattern implementation using decorator can be found [here](https://gist.github.com/dunossauro/f86c2578fe31c4495f35c3fdaf7585bb)

* More pythonic implementation using `__new__` can be found [**here**](https://python-patterns.guide/gang-of-four/singleton/)

```Python
# This is an example of pythonic version of singleton pattern
# A catch with this approach is not to define the __init__ method.
# Note that __init__ method will be called everytime `__new__` method is called
# even though `__new__` is going to return the same instance.
class OneOnly:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(OneOnly, cls).__new__(cls, *args, **kwargs)
        return cls._singleton
```

* But this approach is less readable to a python programmer. One has to look at the class's `__new__` documentation to know that it returns a singleton.

* This [section of the article](https://python-patterns.guide/gang-of-four/singleton/#verdict) discusses the drawbacks of the above implementation.

> A pattern you have to work around is generally a pattern you should avoid.

## Singleton antipattern

* Just because I need some data to be accessed globally, I should not make the object a singleton (Very similar to using inheritance for code reuse).

---

## Alternative patterns to Singleton

### [Borg pattern](http://www.aleax.it/Python/5ep.html)

* Isolate objects and their state. Any number of objects with shared state is similar to having a single instance.

> From the television show Star Trek: The Next Generation. The Borg are a hive-mind collective: “we are all one.”

Reference implementation of Borg pattern can be found [here](https://github.com/faif/python-patterns/blob/master/patterns/creational/borg.py#L51)

### Global state pattern

* Module level variables can mimic singletons.

* Global variables can be used to define constants, immutable objects like tuple, frozenset, and also mutable objects in some cases.

* Assigning objects like file contents or network connections that increase the module import time are not recommended to be made available as module global variables. Even if they were to be made as module global variable, those operations should be **performed lazily** when those global variables are first accessed.

---

## References

* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
* [Singleton Design pattern theory](https://sourcemaking.com/design_patterns/singleton)
* [Singleton design pattern: Patterns and Idioms](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html)
* [Borg pattern example](https://github.com/faif/python-patterns/blob/master/patterns/creational/borg.py)
* [Singleton pattern review in python](https://python-patterns.guide/gang-of-four/singleton/)
* [Global object pattern](https://python-patterns.guide/python/module-globals/)

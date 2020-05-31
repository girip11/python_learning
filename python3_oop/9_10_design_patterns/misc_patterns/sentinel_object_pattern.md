# The Sentinel Object Pattern

> Every name in Python either does not exist, or exists and refers to an object

Sometimes it is necessary to differentiate between an argument that has not been provided, and an argument provided with the value `None`. For that purpose, we create what's called a **'sentinel value'**.

## Null object pattern

> * “Null objects” are real, valid objects that happen to represent a blank value or an item that does not exist
> * The standard Python sentinel is the built-in `None` object, used wherever some alternative needs to be provided to an integer, float, string, or other meaningful value.

## Uses

For most programs it is entirely sufficient, `None` can't be used as null object for all the situations. Situations that demand a different sentinel objects are as follows

> * A general purpose data store doesn’t have the option of using `None` for missing data if users might themselves try to store the `None` object.
> * The second interesting circumstance that calls for a sentinel is when a function or method wants to know whether a caller supplied an optional keyword argument or not. Usually Python programmers give such an argument a default of None. But if your code truly needs to know the difference, then a sentinel object will allow you to detect it.

## Examples

* For example, `NullHandler` in python's standard library `logging` module follows the null object pattern. This sort of null object value adds better readability compared to the `None` object.

* From this [**article**](https://stackoverflow.com/questions/39313943/sentinel-object-and-its-applications), `dataclasses` module using `_MISSING_TYPE` as a sentinel object.

> But whatever the application, the core of the Sentinel Object pattern is that it is the object’s identity — not its value — that lets the surrounding code recognize its significance. If you are using an equality operator to detect the sentinel, then you are merely using the Sentinel Value pattern described at the top of this page. The Sentinel Object is defined by its use of the Python is operator to detect whether the sentinel is present.

* Using `sentinel = object()` as sentinel value makes debugging harder since `repr(sentinel)` does not print anything useful.

```Python
class _NoDefault(object):
    def __repr__(self):
        return '(no default)'
NoDefault = _NoDefault()
del _NoDefault

def getuser(username, default=NoDefault):
    pass
```

* Another example using the sentinel from the `unittest.mock` package. But the drawback is to include the `unittest` package in the production code.

```Python
from unittest.mock import sentinel
NotSet = sentinel.NotSet

# prints 'sentinel.NotSet'
repr(NotSet)
```

* Another approach is to define a class and use that class itself as sentinel object.

```Python
class NotSet:
    def __repr__(self):
        return 'NotSet'

# prints NotSet
repr(NotSet)

# PS: Remember to use the class _itself_.
def fn(default=NotSet):
    pass
```

We can also use sentinels from other python packages like

* [sentinels](https://pypi.org/project/sentinels/)
* [sentinel](https://pypi.org/project/sentinel/)

---

## References

* [The Sentinel Object Pattern](https://python-patterns.guide/python/sentinel-object/)
* [Pro-Tip – Sentinel values in Python](https://www.revsys.com/tidbits/sentinel-values-python/)
* [Default Parameter Values in Python](http://effbot.org/zone/default-values.htm)
* [The Magic Sentinel](http://www.ianbicking.org/blog/2008/12/the-magic-sentinel.html)

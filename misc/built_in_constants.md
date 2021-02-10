# Builtin constants in Python

* `True`
* `False`
* `None`
* `Ellipsis`
* `NotImplemented`
* `__debug__`

## Ellipsis

* `Ellipsis` is a singleton object of the type `ellipsis`.

```Python
type(Ellipsis)

x = ...
print(x)
type(x)
```

### Usage

* In type hinting.

```Python
from typing import Callable, Tuple

def add(a: int, b: int) -> int:
    return a + b

some_func: Callable[..., int] = add

# represent homogenrous tuple
str_only_tuple: Tuple[str, ...]
```

* Ellipsis literal is also used as a no-op placeholder.

```Python
def some_func(arg):
    ...
```

* In some third party libraries like [numpy when slicing ndarrays](https://python-reference.readthedocs.io/en/latest/docs/brackets/ellipsis.html).

```Python
import numpy as np

arr = np.arange(16).reshape(4, 2, 2)

# Take only the first column from all matrices
arr[..., 1]
# above is same as
arr[:, :, 1]
```

## `NotImplemented`

* Its a sole instance of `NotImplementedType`.

> Special value which should be returned by the binary special methods (e.g. __eq__(), __lt__(), __add__(), __rsub__(), etc.) to indicate that the operation is not implemented with respect to the other type; may be returned by the in-place binary special methods (e.g. __imul__(), __iand__(), etc.) for the same purpose. It should not be evaluated in a boolean context. - [Python docs](https://docs.python.org/3/library/constants.html#NotImplemented)

```Python
class B:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, B):
            return self.value + other.value

        print(f"Add operation with type {other.__class__.__name__} is not supported by {type(self).__name__}")
        return NotImplemented

class A:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, (A, B)):
            return self.value + other.value

        print(f"Add operation with type {other.__class__.__name__} is not supported by {type(self).__name__}")
        return NotImplemented

a = A(1)
b = B(1)

print(a + b)
print(b + a) # raises exception
```

## `__debug__`

* This is of `bool` type and is set to `True` if the python interpreter was not started with `-O` flag (optimization mode).

---

## References

* [Built-in Constants](https://docs.python.org/3/library/constants.html)
* [Ellipsis](https://docs.python.org/dev/library/constants.html#Ellipsis)
* [NotImplemented](https://s16h.medium.com/pythons-notimplemented-type-2d720137bf41)

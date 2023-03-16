# Generics with type hinting in Python

## [Generics](https://docs.python.org/3/library/typing.html#user-defined-generic-types)

- Parameterize generics using `TypeVar`.

```Python
from typing import Type, TypeVar

# create a type parameter
T = TypeVar('T')

def deserialize(json: str, cls: Type[T]) -> T:
    pass
```

- User defined class using generics can be created

```Python
from typing import Generic, TypeVar
# create a type parameter
T = TypeVar('T')

# Below is equivalent to class Myclass[T] in C#
# This makes T valid as a type within the class body.
class Myclass(Generic[T]):
    pass
```

- Generic constraints

```Python
# S can be of type S or int or str
S = TypeVar('S', int, str)
```

---

## References

- [Generics](https://mypy.readthedocs.io/en/stable/generics.html)

# Protocols in Python

- Are useful when we want to type the duck typing behavior (structural typing)
- For instance, in python we have iterable protocol which is any object with `__iter__` is an iterable, while in the iterator protocol any object with `__iter__` and `__next__` is an iterator.

- This can save from scenarios which require defining complex type hierarchies when structural subtyping would solve it.

```Python
from typing import Protocol

class Closeable(Protocol):
    def close(self) -> None:
        ...

# we can pass any object that implements `close` method
def fetch_data(connection: Closeable) -> str:
    ...

```

---

## References

- [Protocols and structural subtyping](https://mypy.readthedocs.io/en/stable/protocols.html)
- [Protocols and duck typing](https://blog.logrocket.com/understanding-type-annotation-python/)
- [PEP 544](https://peps.python.org/pep-0544/)

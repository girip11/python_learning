# SimpleNamespace in Python

* Provides attribute access to the namespace.
* Additionally provides `__repr__` and `__eq__` methods.

```Python
from types import SimpleNamespace

john = SimpleNamespace(name="John", age=20)
jane = SimpleNamespace(name="Jane", age=20)

print(john.name, jane.name)
print(john == jane)
print(repr(john))
```

---

## References

* [`types.SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace)
* [Implementing data objects in Python](https://dbader.org/blog/records-structs-and-data-transfer-objects-in-python)

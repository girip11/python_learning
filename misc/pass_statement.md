# `pass` statement in python

## Uses

* Can act as a placeholder for block of code in functions, methods, classes etc.
* Very useful in scaffolding.
* Useful when testing certain code paths in functions.
* Implementing abstract methods in abstract classes.
* When we want to catch an exception but ignore it after.
* Useful  in `if … elif` Chains

## Alternatives to pass

* Using docstrings
* Raising exception using `raise NotImplementedError`
* Using Ellipsis. Helpful in defining functions in **.pyi** files.

```Python
def some_func(a: int, b:int) -> int:
    ...
```

---

## References

* [The pass Statement](https://realpython.com/python-pass/)

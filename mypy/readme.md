# Using mypy

## Type debugging

- `reveal_type(obj)`(special mypy function) can be placed in the source file we need to inspect. When we run `mypy` it will reveal the object type.

- In unchecked functions, when we use `reveal_type`, it returns `Any`

- Type hints can be added to the project externally using the stub files `.pyi` files.

---

## References

- [Python type checking with mypy](https://dev.to/tusharsadhwani/the-comprehensive-guide-to-mypy-561m)

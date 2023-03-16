# Stubs and typeshed

- For third party packages, we can create stub files that just contain the type information for use by third party type checkers.
- Typeshed is a github repository that contains the stub files for various python packages that don't have type hints in the codebase.
- Python type checkers - mypy, pyre(Facebook), pytype(Google) and pyright(Microsoft)

- Pydantic is a library that can be used to enforce type checks at the runtime using the type annotations.

- Type annotations also greatly help python to compile to low level code like Cython or [mypyc](https://github.com/mypyc/mypyc).

---

## References

- [Python typing](https://realpython.com/python-type-checking/)

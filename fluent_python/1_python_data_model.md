# Python data model

- Special methods are referred to as `dunder methods`
- `in` operator first looks for `__contains__` method. If that's not present, then it does a sequential scan(iterable).
- From python 3, `class SimpleClass(object)` implicits to `class SimpleClass`.

**NOTE** - Special methods are meant to be called by the python interpreter.

> Normally, your code should not have many direct calls to special methods. Unless you are doing a lot of metaprogramming, you should be implementing special methods more often than invoking them explicitly.
> Avoid creating arbitrary, custom attributes with the `__foo__` syntax because such names may acquire special meanings in the future, even if they are unused today.

## `__repr__` and `__str__`

- The string returned by `__repr__` should be unambiguous and, if possible,match the source code necessary to re-create the object being represented. To be more precise, if we give the `__repr__` output to `eval` we should have the expression evaluated.

- `__str__` returns string representation that is human readable.

- Python uses `__repr__` when no custom `__str__` is present.

## `__bool__`

- By default, instances of user-defined classes are considered truthy, unless either `__bool__` or `__len__` is implemented.
- Basically, `bool(x)` calls `x.__bool__()` and uses the result.

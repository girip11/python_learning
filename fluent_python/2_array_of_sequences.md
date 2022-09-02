# Array of sequences

## Container and flat sequences

- Container sequences - hold reference to the objects. `list`, `tuple` and `collections.deque`
- Flat sequences - holds the objects within their memory. Can hold only the primitive types. `str`, `bytes`

## Mutability

- `str`, `tuple` and `bytes` are immutable while others are mutable.

## Collection abstract classes

`collections.abc` contains definitions of abstract classes for `Iterable`, `Iterator` etc

- `Iterable` exposes `__iter__`
- `Iterator` exposes `__iter__` and `__next__`
- `Sized` exposes `__len__`
- `Container` exposes `__contains__`. This is invoked when used with `in` operator.
- `Reversible` exposes `__reversed__`
- `Sequence` exposes `__getitem__`, `__contains__`, `__iter__`, `__reversed__`, `index` and `count`. Thus `Sequence` inherits from `Container`, `Iterable` and `Reversible`.
- Similarly we have abstract class for `MutableSequence` which adds `__setitem__` and `__delitem__` methods as well.

## List comprehensions (listcomps)

> A quick way to build a sequence is using a list comprehension (if the target is a list) or a generator expression (for all other kinds of sequences).

- A listcomp is meant only for creating a new `list`.

> If you are not doing something with the produced list, you should not use that syntax. Also, try to keep it short. If the list comprehension spans more than two lines, it is probably best to break it apart or rewrite as a plain old for loop.

- Variables defined inside comprehensions have their own local scope from python 3.

- List comprehensions can iterate on any sequence or any iterable.

- `map` and `filter` can be achieved using list comprehensions.

```Python
color_codes = ["R", "G", "B"]
colors = {
    "R": "Red",
    "G": "Green",
    "B": "Blue"
}

color_names = [colors[code] for code in color_codes]
```

## Generator expressions (genexps)

- To build a sequence of any type we need to use genexps because comprehensions build either `list` or `dict`.

- Memory efficient as it computes the elements lazily.

## Tuples

- Tuples can be used as records but without field names.

**NOTE** - If you write internationalized software, `_` is not a good dummy
variable because it is traditionally used as an alias to the get
`text.gettext` function.

### Unpacking

```Python
# tuple unpacking
a, b = (1, 2)

# unpack excess args, but only one variable with * can be used
# *arg can appear anywhere in the variables position
a, b, *rest = [1, 2, 3, 4, 5]
```

- Tuple unpacking works with nested tuples too.

```Python
city = ("Chennai", "India", (13.0827, 80.2707))

# unpacking
name, country, (lat, long) = city
```

### Named tuples

- `collections.namedtuple` or python 3.6 onwards use `typing.NamedTuple`

```Python
from typing import NamedTuple

class SomeNamedTuple(NamedTuple):
    a: str
    b: int
```

`SomeNamedTuple` in the above example has the following useful attributes due to it inheriting from `NamedTuple`.

- `_fields`
- `_asdict`
- `_replace`
- `_make`

### Tuples as immutable lists

- Tuples can also be viewed as immutable lists.

## Slicing

- `start: stop: [step]`. step is optional and by default its 1.

> The notation `a:b:c` is only valid within `[]` when used as the **indexing or subscript operator**, and it produces a slice object: `slice(a, b, c)`.

- Python invokes `seq.__getitem__(slice_object)` to evaluate slice syntax.

### Multidimensional slicing

- `a[i, j]` - multidimensional index
- `a[m:n, k:l]` - multidimensional slicing

Multidimensional slicing is used in `numpy` package.

```Python
# this is how it works
from collections.abc import Sequence

class MySeq(Sequence):
    def __getitem__(self, index):
        print(index)
        # implementation
    def __len__(self) -> int:
        return 0

seq = MySeq()
# this outputs (1,2)
seq[1, 2]

# this outputs (slice(1,2,None), slice(3,4,None))
seq[1:2, 3:4]
```

> The built-in sequence types in Python are **one-dimensional**, so they support only one index or slice, and not a tuple of them.

### `Ellipsis` object

- `...` alias to `Ellipsis` is the only instance of `ellipsis` class.

- `Ellipsis` is a sentinel. `Ellipsis` and `ellipsis` are found under `builtins` module

> NumPy uses `...` as a shortcut when slicing arrays of many dimensions; for example, if `x` is a fourdimensional array, `x[i, ...]` is a shortcut for `x[i, :, :, :,]`.

### Slice to update mutable sequences

- Slices can be used to change the mutable sequences in place.
- For these operations to work the following methods are required to be present `__setitem__` and `__delitem__`. If you are implementing a custom class, inherit from `collections.abc.MutableSequence`

```Python
arr = [1, 2, 3, 4, 5]

# update
arr[1: 3] = [10, 11]

# delete
del arr[2:4]
```

### `+` and `*` with sequences

- `+` - appends sequences
- `*` - expands the list by that many times. `[0] * 3` yields `[0, 0, 0]`.

Both always produce a new list.

Never use `*` when items in the sequences themselves are mutable objects, because the references remain the same. List comprehension is the best way to do this.

```Python
# BAD
expanded = [[]] * 3

# yields True
expanded[0] is expanded[1]

# will reflect in all the inner lists since the reference is same
expanded[0].append(1)

# GOOD
expanded = [[] for _ in range(3)]
```

**NOTE** - Putting mutable item inside a tuple is not recommended.

To know about how a python instruction gets executed(instructions corresponding to python code), we can use the `dis` python module.

```Python
from dis import dis
dis("s[a] += b")
```

- `INPLACE_ADD` instruction corresponds to calling `__iadd__`

## `bisect` module

- `bisect(haystack, needle)` returns index to insert needle in a haystack which is a sorted sequence. Does a binary search.
- `insort` - searches a sorted sequence and inserts the needle

## `array` module

- python `array` is as lean as C array. Useful when we want to store a collection of numbers(homogenous items).

- For numeric arrays with binary data, we could use `bytes`(immutable byte array) and `bytearray`(mutable)

## Memory views

- Shared memory sequence type that lets you handle slices of arrays without copying bytes.

Other useful modules are `deque`, `queue`, `multiprocessing`, `asyncio`, `heapq`.

## References

- [Online Python tutor](www.pythontutor.com)

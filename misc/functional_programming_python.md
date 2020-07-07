# Functional programming in python

> Functional style **discourages functions with side effects** that modify internal state or make other changes that aren’t visible in the function’s return value. Functions that have no side effects at all are called **purely functional**. Avoiding side effects means not using data structures that get updated as a program runs; every function’s output must only depend on its input.

* **Pure functions** - accepts input and returns output without modifying the state of the system.
* **Immutability** - cannot change the object's state once it is created. Ex: String and tuple in python are immutable.
* **Higher order functions** - Functions that can accept another function as input parameter and return a function as output. For instance, `map` and `filter` are examples of higher order functions.

* [Generator expressions](../python3_oop/9_iterator_pattern.md) and list comprehensions can be used as alternative to the lambdas, `map` and `filter` functions.

**NOTE**: In python, people avoid using lambdas and instead use functions for readability purposes.

## Builtin functions

* [`map(f, iter1, iter2, ...)` and `filter(predicate_function, iter)`](../python3_absolute_beginners/chapter_6_lambda_functions.md)

* `enumerate(iter, start = 0)`

```Python
for index, value in enumerate(range(10, 20)):
    print(f"Index: {index}, value: {value}")
```

* `all(iter)` and `any(iter)`

```Python
import random

rand_arr = [random.randint(0,10) *  i for i in range(0, 10)]
print(rand_arr)

# all elements in the iterable should evaluate to True
print(all(rand_arr))

# atleast 1 element in the iterable should evaluate to True
print(any(rand_arr))
```

* `zip(iter1, iter2, ...)`. Performs lazy evaluation (next element is fetched only when needed). If the iterables are of different length, the output iterator is truncated to the length of the shortest iterable.

```Python
for i in zip(range(0, 10), range(10, 20)):
    print(i)
```

* `sorted(iter, key = None, reverse = False)`. Key can accept a function to customize the sort order. Returns a new list with its contents sorted.

```Python
import random

arr = random.sample(range(100), 5)
print(arr)
print(sorted(arr))
print(sorted(arr, reverse = True))
```

* `reversed(iter)` - returns an iterator

```Python
import random

arr = random.sample(range(100), 5)
print(arr)

print(list(reversed(arr)))
```

## `operator` module

* `dir(operator)` - to list the functions inside the operator module. Contains the python arithmetic, logical, bitwise, relational, object equality operators as functions.

```Python
from functools import reduce
import operator

sum = reduce(operator.add, range(1, 10))
print(f"Sum: {sum}")
```

## `itertools` module

## Creating new iterators

* `itertools.cycle(start = 0, step = 1)` - iterator which returns infinite stream of numbers starting from start.

```Python
from itertools import count
counter = 0
for i in count(10, 5):
    print(i)
    counter +=1
    if counter >= 100:
        break
```

* `itertools.cycle(iter)` - returns a new iterator that endlessly cycles throught the elements in the iterable passed as input.

```Python
from itertools import cycle

counter = 0
for i in cycle(range(1, 10)):
    print(i)
    counter +=1
    if counter >= 100:
        break
```

* `itertools.repeat(elem, [n])` returns an iterator that returns the provided element n times, or returns the element endlessly if n is not provided.

```Python
import itertools

# repeat is a class that has __next__() method implemented
# hence an instance of repeat can act as an iterable.
help(itertools.repeat)
dir(itertools.repeat(1,2))
```

* If we have a scenario to sequentially iterate through multiple iterables one after the other, we can use the `itertools.chain(iter1, iter2,...)` method.

```Python
import itertools

for i in itertools.chain(range(1,5), range(10, 20)):
    print(i)
```

* `itertools.islice(iter, [start], stop, [step])` returns a stream that’s a slice of the iterator. **islice doesnot take keyword arguments**

**NOTE**: We **can’t use negative** values for start, stop, or step.

```Python
from itertools import islice

# Stop with 7 iterations
for i in islice(range(10), 7):
    print(i)

# below is equivalent to for syntax in C
# for (i = 3; i < 9; i += 2) {
#      do-something
# }
for i in islice(range(10), 3, 9, 2):
    print(i)
```

* `itertools.tee(iter, [n])` replicates an iterator; it returns `n` independent iterators that will all return the contents of the source iterator. If you don’t supply a value for n, the default is 2

```Python
from itertools import tee

iter1, iter2 = itertools.tee(range(1, 10), 2)

for i, j in zip(iter1, iter2):
    print(i, j, sep=',')

```

* `itertools.accumulate(iter, func)` - returns an iterable when each element is the result (partial result) of applying the `func` on previous elements in the input iterable

```Python
from itertools import accumulate
import operator

#  Prints [1, 3, 6, 10, 15, 21, 28, 36, 45]
for i in accumulate(range(1, 10), func=operator.add):
    print(i)
```

* `itertools.starmap(func, iter)` - iterable should return a stream of **tuples**. (Try to remember this function as *map that can do map on a n-tuple)

```Python
from operator import add
from itertools import starmap

# starmap returns an iterator
for i in starmap(add, zip(range(1, 10), range(11, 20))):
    print(i)
```

* `itertools.zip_longest(iter1, iter2, ... , [fillvalue=None])` - zips all the iterable elements in to n-tuple till the longest iterable is exhausted unlike the builtin zip which stops with the smallest iterable.

```Python
for k, v in itertools.zip_longest(range(1,10), range(15, 20), fillvalue=1):
    print(k, v, sep=":")
```

## Selecting elements

* `itertools.filterfalse(predicate_func, iter)` - return those elements in the iterable for which the predicate function returns `False`.

```Python
from itertools import filterfalse
for i in filterfalse(lambda a: a>10, range(1,15)):
    print(i)

```

* `itertools.takewhile(predicate_func, iter)` - returns elements from the iterable till the predicate returns `False`.

```Python
from itertools import takewhile

for i in takewhile(lambda n: n <= 25, range(1, 50)):
    print(i)
```

* `itertools.dropwhile(predicate_func, iter)` - drops elements from the iterable till the predicate returns `False`.

```Python
from itertools import dropwhile

for i in dropwhile(lambda n: n <= 25, range(1, 50)):
    print(i)
```

## Combinatoric functions

* `itertools.combinations(iter, r)`- returns nCr.
* `itertools.permutations(iter, r=None)`- returns nPr.

## Grouping elements

* `itertools.groupby(iter, key_func=None)` - By default the key is simply the element itself.

* Returns an iterator containing a 2-tuple of `(Key, iterable_containing_elements_grouped_by_key)`

* For groupby to work, the input iterable should be **sorted**

```Python
from itertools import groupby

test_arr = ['aab', 'aba', 'aab']

# Each element will become the key and there will be 3 keys
# since the array is not sorted
print("Input iterable without sorting")
for i in groupby(test_arr):
    print(f"Key: {i[0]}")
    print(f"Value: { [j for j in i[1]] }")

# With the input iterable sorted, same keys will be grouped.
# this groupby will contain only 2 keys
print("Input iterable sorted")
for i in groupby(sorted(test_arr)):
    print(f"Key: {i[0]}")
    print(f"Value: { [j for j in i[1]] }")
```

> * `groupby()` collects **all the consecutive elements** from the underlying iterable that have the same key value, and returns a stream of 2-tuples containing a key value and an iterator for the elements with that key.
> * Note that the returned iterators also use the underlying iterable, so you have to consume the results of iterator-1 before requesting iterator-2 and its corresponding key.

```Python
# input sorted by string length
test_arr = ["123", "aab", "1234", "abcd"]

def key_func(e):
    return len(e)

for i in itertools.groupby(test_arr, key_func):
    print(i[0], list(i[1]))
```

## `functools` module

* `partial(func, arg1, arg2,..., kwarg1=value1,..)`

> For programs written in a functional style, you’ll sometimes want to construct variants of existing functions that have some of the parameters filled in. Consider a Python function f(a, b, c); you may wish to create a new function g(b, c) that’s equivalent to f(1, b, c); you’re filling in a value for one of f()’s parameters. This is called “**partial function application**”.

```Python
import functools

def log(message, subsystem):
    """Write the contents of 'message' to the specified subsystem."""
    print('%s: %s' % (subsystem, message))

server_log = functools.partial(log, subsystem='server')

# The resulting object is callable, so you can just call it to
# invoke function with the filled-in arguments.
server_log('Unable to open socket')
```

* `functools.reduce(func, iter, [initial_value])` - Initial value gets applied to the function(as in func(initial_value, first_value)), it is useful when the input iterable is empty.

```Python
from functools import reduce
from operator import add
# Initial value should be such that when applied to
# nonempty iterable, it should not alter the result

# prints 45 (45 + 0 = 45)
print(reduce(add, range(1, 10), 0))

# prints 46 (45 + 1 = 46)
print(reduce(add, range(1, 10), 1))

# prints 0. without the initial value, reduce raises TypeError
print(reduce(add, [], 0))
```

* `operator` module can be handy when using `reduce`.

* Performance of `reduce` against other builtin functions like `sum`, `all` etc can be found [here](https://realpython.com/python-reduce-function/).

> Use functools.reduce() if you really need it; however, 99 percent of the time an explicit for loop is more readable. -[What’s New In Python 3.0 guide](https://docs.python.org/3/whatsnew/3.0.html)

---

## Reference

* [Python docs: Functional programming](https://docs.python.org/3/howto/functional.html)
* [Functional Programming in Python](https://stackabuse.com/functional-programming-in-python/)

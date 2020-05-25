# Generators

* Enables lazy computation. Items are produced on demand. Generators consume less memory.

* Use of **yield** in a function makes it a generator.

* Generator object is iterable.

## Generator Expressions

* Generators defined by comprehensions

* These expressions can be passed to any function that can work with iterables.

> **NOTE**: Always pass a generator expression, instead of a list comprehension, to functions that expect iterables, such as `min()`. This is more efficient and pythonic.

```Python
# An example to demonstrate the usage of a generator expression
# for iteration.
def double(n: int) -> int:
    return i * 2

doubler = (double(i) for i in range(10))

# Generator expressions can be used in iterations
for num in doubler:
    print(doubler)
```

## `next()` builtin

* `next(iterator, [default])` - Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.

## Generator functions

```Python
def sequence(start=0):
    while True:
        yield start
        start += 1
```

## [Itertools module](../misc/functional_programming_python.md)

* `itertools` module has several utility functions that are generators.

## Applications

* `itertools.tee` can be used whenever we need to iterate many times over an iterator.

* Use generators to flatten iteration over multidimensional array

```Python
# Itertools module gives a method called product which
# returns the cartesian product of the iterables passed.

# This is just an example to demonstrate how we can flatten
# iteration over multidimensional array or nested for loops
def cartesian_product(iter1, iter2):
    for i in iter1:
        for j in iter2:
            yield (i,j)

for entry in cartesian_product(range(5), range(6,10)):
    print(entry)
```

> Try to simplify the iteration as much as possible with as many abstractions as are required, flatting the loops whenever possible.

## Iterator pattern in python

Generators are iterables since they implement both `__iter__` and `__next__` magic methods.

* Iterable - an object that can be iterated using `for .. in`. This should implement `__iter__` method.
* Iterator - an object that knows how to produce a series of values one at a time. Generators are iterators(in the sense they also produce one item at a time). Iterators should implement `__next__` magic method.
* Sequence - an object that can be iterated using `for .. in`. This object should implement `__len__` and `__getitem__` magic methods.

* In the `for .. in` loop, python interpreter checks if the object is an iterable. If not then it checks if the object is a sequence.

## Coroutines

Following methods are available on generator objects to provide support for coroutines.

* `close()`
* `throw(ex_type[, ex_value, ex_traceback])`
* `send(value)`

Calling `close()` method on the generator object raises `GeneratorExit` exception which can be handled inside the generator. This is used for performing cleanup/finishing tasks in the generator.

When we call `throw` on the generator object, the exception can be caught and handled within the generator code.

`send` method distinguishes generator from a coroutine. Coroutines pause at each `yield` expression in the generator function and resume after each call to `send` from the outside. Imagine each `.send` to behave like an independent function call(passing argument and returning values)

```Python
def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)

it = minimize()
next(it)            # Prime the generator
print(it.send(10))
print(it.send(4))
print(it.send(22))
```

For coroutines, calling `.send(None)` will be equivalent to calling `next()`. On calling `.send`  everytime, the coroutine is advanced by one iteration. So we can use `.send` on coroutines to advance it. Contextually `next()` is preferred on iteration scenarios.

```Python
def stream_numbers(default_page_size  = 10):
     retrieved_data = None
     page_size = default_page_size
     try:
        while True:
            page_size = (yield retrieved_data) or page_size
            print(f"page_size: {page_size}")
            retrieved_data = list(range(0, page_size))
     except GeneratorExit:
        print("Close method on this generator is called")

cor = stream_numbers()
# first time we have to advance the coroutine
next(cor)

# This should return an array from [0-9]
print(cor.send(None))

# This should return an array from [0-19]
print(cor.send(20))

cor.close()

# Both raise StopIteration exception after the coroutine is closed.
next(cor)
cor.send(100)
```

>Sending values to the coroutine only works when this one is suspended at a yield statement, waiting for something to produce. For this to happen, the coroutine will have to be advanced to that status. The only way to do this is by calling next() on it. This means that before sending anything to the coroutine, this has to be advanced at least once via the next() method.

* Though coroutines are built on top of generators, with coroutines, we should think of suspending the state rather than iteration.

## Delegating into smaller coroutines

* `yield from` statement is used
* `yield from` can work over **any iterable**(including generators, generator expressions).

Usecases

* Capturing value **returned** by a subgenerator. In normal generator functions, the return value is stored in the `StopIteration` exception object.
* Sending and receiving data to and from a subgenerator.

## Asynchronous programming

* Using `async` and `await`. Coroutines are awaitable.

---

## References

* [Clean code in python by Mariano Anaya](https://www.oreilly.com/library/view/clean-code-in/9781788835831/)
* [Consider Coroutines to Run Many Functions Concurrently](https://effectivepython.com/2015/03/10/consider-coroutines-to-run-many-functions-concurrently)

# The **iterator** pattern

## Iterators in Python

* An object (aka container object in the below context) is called **iterable** if you can **get an iterator** for it.

* Container object should implement `__iter__()` method. `iter(container_object)` returns the iterator object. `iter()` method documentation can be found [here](https://docs.python.org/3/library/functions.html#iter)

* Iterator is an object in python that has both `__iter__()` and `__next__()` special methods implemented.

* `next(iterator)` - should return the next object in the sequence.If there are no further items, raise the `StopIteration` exception.

**NOTE**: Once an iterator’s `__next__()` method raises `StopIteration`, it must continue to do so on subsequent calls. **Implementations that do not obey this property are deemed broken**.

* [Iterator Protocol](https://docs.python.org/3/library/stdtypes.html#iterator.__next__). Iterator abstract base class in module `collections.abc` defines the iterator protocol.

```Python
# iterating on an iterable using for loop

# for first uses the iter() to get the iterable and invokes next() to continue further iterations.

# iterable on iter() returns an iterator
# iterator on iter() returns itself.
for item in iterable:
  print(item)
```

## `itertools` module

This module contains helpful functions for operating on iterables.

```Python
import itertools

# lists all useful methods for working with iterables.
dir(itertools)

def squareValue(value, power):
  return value ** power

gen = itertools.starmap(squareValue, [(1,2), (2,2), (3,3)])

for value in gen:
  print(value)
```

## Comprehensions

Comprehensions - concise, highly optimized for creating list, set or dict from a sequence. can perform map, filter operations.

### List comprehensions

 List comprehensions **faster compared to looping over the list**.

```Python
# map a list of strings to list of integers containing their length
input = ['hello', 'this', 'foo', 'bar']
output = [len(entry) for entry in input]

# filter operation
# take only strings with length of atleast 4 characters
words = [entry for entry in input if len(entry) >= 4]
```

### Set and Dictionary comprehensions

* Enclose the expression inside `{}`.

```Python
input = [1, 2, 5, 3, 3, 8, 2, 3]

# set comprehension
unique_values = {n for n in input}

# dictionary comprehension
input = ['hello', 'this', 'foo', 'bar']
output = {entry: len(entry) for entry in input}
```

## Generator expressions

> Generators are iterators that you can iterate over **only once**. Generators donot store all the values in memory and generate the values on the fly. -[Stackoverflow Yield usage](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
> List comprehensions aren’t useful if you’re working with iterators that return an infinite stream or a very large amount of data. Generator expressions are preferable in these situations - [Python Functional programming](https://docs.python.org/3/howto/functional.html)

* Same syntax as comprehension, but `()` are used instead of `[]` or `{}`. In generator expressions, the final container **is not created**. **Memory efficient**.

```Python
input = [1, 2, 4, 5, 6, 2, 9]

# the computation is yet to take place
gen_exp = (e for e in input if e >= 5)
print(type(gen_exp))

# this gen_exp can be iterated over only once.
for item in gen_exp:
  print(item)
```

* Generator expressions always have to be written inside parentheses, but the parentheses signalling a function call also count.

```Python
# generator expression returns an iterable that is passed to the max function
max(i for i in random.sample(range(200), 25))
```

## Generator and yield keyword

> * Generators are a special class of functions that simplify the task of writing iterators. Regular functions compute a value and return it, but generators return an iterator that returns a stream of values.
> * The big difference between `yield` and a `return` statement is that on reaching a yield the generator’s state of execution is suspended and local variables are preserved.
> [- Python Functional programming](https://docs.python.org/3/howto/functional.html)

* Function with `yield` keyword when invoked returns a **generator object** that **follows the iterator protocol.**

* Generators can be thought of as resumable functions. On encountering the `yield` statement, function returns the value to the caller, but when `next()` is called on that function, function execution resumes from the line of code **after the yield statement**.

```Python
def get_generator(n):
    for i in range(n):
        yield i

# storing the results by unpacking
a, b, c = get_generator(3)

for i in get_generator(5):
    print(i)

gen = get_generator(4)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
```

* Function execution pauses at the `yield` statement. Whenever `__next__` is called, generator function runs code placed following the yield statement till the **next yield statement**.

* A generator function can have multiple yield calls.

```Python
def gen_func(n):
    print("Hello")
    for i in range(n):
        print('Before yield')
        yield i
        print('After yield')

    print("end")

gn = gen_func(5)

# Only when iterating over the generator object, the function execution
# starts. For every iteration, the execution resumes after the statement
# following the yield
for i in gn:
    print(f"gn: {i}")

# output
# Hello
# Before yield
# gn: 0
# After yield
# Before yield
# gn: 1
# After yield
# Before yield
# gn: 2
# After yield
# Before yield
# gn: 3
# After yield
# Before yield
# gn: 4
# After yield
# end
```

* Wherever in Python, iterable is expected, generators work (duck typing).

```Python
def filter_values(input):
  for n in input:
    if n >=5:
      yield n

input = [1, 2, 5, 3, 3, 8]
generator = filter_values(input)
print(type(generator))   # prints 'generator'

# observe ths class generator has __iter__ and __next__ implemented.
dir(generator)

for value in filter_values(input):
  print(value)
```

> * Inside a generator function, `return value` causes `StopIteration(value)` to be raised from the `__next__()` method. Once this happens, or the bottom of the function is reached, the procession of values ends and the generator cannot yield any further values

## Yield items from another iterable

```Python
# read lines from a file
def processLog(file):
  with open(file) as input_file:
      yield from (log_line for log_line in input_file)
```

`yield from` used with generator expressions, generators(another generator or recursive one)

## Coroutines

* Coroutines can be entered, exited, and resumed at many different points.

* Coroutines are similar to generators, while generators can't have data passed to it, **using coroutines data can be passed to the generators.** (generators produce data, coroutines can consume data)

> The thing that is really confusing for many people is the order in which this happens:
>
> * yield occurs and the generator pauses
> * send() occurs from outside the function and the generator wakes up
> * The value sent in is assigned to the left side of the yield statement
> * The generator continues processing until it encounters another
yield statement
> -From the book Python3 Object Oriented Programming

`send()` method does the following

* pass value from outside generators
* performs function of `next()` (i.e) returns the value obtained from the next yield statement and pauses the execution.

```Python
# coroutine_example
def counter():
  count = 0
  while True:
    step = (yield count)
    if(step == None or (not isinstance(step, int))):
      break
    count += step

coroutine = counter()
print(type(coroutine))

# prints 0 and pauses
print(next(coroutine))

for n in range(1, 20):
  print(coroutine.send(i))

coroutine.send(None)
```

> I recommend that you always put parentheses around a yield expression when you’re doing something with the returned value, as in the above example. The parentheses aren’t always necessary, but it’s easier to always add them instead of having to remember when they’re needed. - [Python Functional programming](https://docs.python.org/3/howto/functional.html)

## Closing coroutines and throwing exceptions

Generator exits by raising `StopIteration`, that propogates through chained iterators and then to the for loop using the generator.

In case of coroutines, caller knows to proceed to next iteration using `send()` method. Hence coroutines are usually closed by calling `close()` method on the coroutine instance.

`close()` call raises `GeneratorExit` exception. Good practice to wrap yield statement inside try .. finally

---

## References

* [Python3 Object oriented programming by Dusty Phillips](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
* [Understanding Python's for statement](http://effbot.org/zone/python-for-statement.htm)
* [Python iterator pattern review](https://python-patterns.guide/gang-of-four/iterator/)

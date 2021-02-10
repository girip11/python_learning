# Generators in python

## Defining a generator function

* Function that contains `yield` keyword becomes a generator function.
* Calling a generator function returns a generator object.

```Python
# Example of never ending generator
def repeat(value):
    while True:
        yield value

# calling generation function returns a generator
gen = repeat(1)
```

* Generator object adheres to the iterator protocol. `next(gen_obj)` yields the next element in the sequence.
* Generators raise `StopIteration` exception when there are no more elements to return. Generators also raise `StopIteration` when `return` statement is encountered.

```Python
# Generator function can also have return statement
# the return value is available as value attribute on the 
# StopIteration exception
def get_range(end):
    for i in range(end):
        yield i

    return end

gen = get_range(3)
print(next(gen))
print(next(gen))
print(next(gen))

try:
    print(next(gen))
except StopIteration as e:
    # return value of the generator function
    print(e.value)
```

* Generator functions can have multiple `yield` statements. Generator functions get paused after the execution of each yield statement.

```Python
# yield temporarily suspends execution of the function and 
# passes back a value to the caller,
def multiple_yields():
    print("Execution start from beginning to end of first yield")
    yield 1
    print("Execution resumes from here to next yield")
    yield 2
    print("Next execution resumes from here to next yield. If no more yield statement, StopIteration is raised")

gen = multiple_yields()
print(next(gen))
print(next(gen))
print(next(gen))
```

## Generator expressions

* Generators are memory efficient compared to comprehensions. Generators generate next element as and when required, while comprehensions materialize before consumption.

```Python
# this is a generator expression
gen = (i for i in range(5))

for i in gen:
    print(i)
```

* Memory profiling generator expression vs list comprehension

```Python
import sys
squared_lc = [i * 2 for i in range(100)]
print(sys.getsizeof(squared_lc)) # 904

squared_genexp = (i ** 2 for i in range(100))
print(sys.getsizeof(squared_genexp)) # 112
```

## Other methods on generators

* `gen_obj.send()` - When the generator function is a coroutine.
* `gen_obj.throw()` - Throw exception from the generator. Stack trace will start with the line containing `yield` statement in the generator.
* `gen_obj.close()` - Closes the generator and it raises `StopIteration`

---

## References

* [How to Use Generators and yield in Python](https://realpython.com/introduction-to-python-generators/)
* [Python generators](https://dbader.org/blog/python-generators)
* [Effective Python Coroutines](https://effectivepython.com/2015/03/10/consider-coroutines-to-run-many-functions-concurrently)

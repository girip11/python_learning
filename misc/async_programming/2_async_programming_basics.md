# Async programming in python

* `async` and `await` are available from python 3.5 onwards.

* `async def` is called a native coroutine while **older coroutines(one where yield returns a value on calling send method)** are referred to as **generator based coroutines**

* Always use **native coroutines** for async IO operations.

**NOTE**: Generator-based coroutines will be removed in **Python 3.10**

## `async` and `await` keywords

* Defining a function with `async` keyword makes that function a **coroutine**

```Python
import asyncio

# say_hello is a native coroutine
async def say_hello(name: str) -> None:
    # wait and say hello
    # Notice await causes the task to stop at sleep
    # and resume again when the sleep gets completed.
    await asyncio.sleep(1)
    print(f"Hello, {name}")

say_hello_obj = say_hello("John")
# This prints coroutine
print(type(say_hello_obj))

# to run the method use asyncio.run
asyncio.run(say_hello_obj)
```

* If we define an async function, it will relinquish its CPU only when the code path reaches a await operation. If there is an async operation that needs any awaiting inside the async coroutine and we haven't not awaited, a `RuntimeWarning` is raised.

```Python
import asyncio

async def say_hello(name: str) -> None:
    # Async operation is not carried out
    # raises a warning 'sleep was never awaited'
    asyncio.sleep(1)
    print(f"Hello, {name}")

async def async_tasks(names):
    await asyncio.gather(*[say_hello(name) for name in names])

# This prints the greetings to the names in order
# without sleeping
asyncio.run(async_tasks(["John", "Jane", "Alice"]))

# Using synchronous operations inside an async method
# will also make it behave like a synchronous method
# because the task will yield its control only when
# an await is encountered
import time
async def say_hello(name: str) -> None:
    # Async operation is not carried out
    # raises a warning 'sleep was never awaited'
    time.sleep(1)
    print(f"Hello, {name}")
```

* Using `await` is a way of the task notifying the **event_loop or the coordinator**, that it is blocked on some IO. Event loop can hand over the CPU to the next task in the queue.

* Similar to `async def`, `async with` and `async for` are available.

## Rules and restrictions on async and await

* `await` can only be used inside `async def`.
* `yield from` cannot be used inside `async def`
* Inside `async def`, we can use `await` and/or `return`(if we need the coroutine to return a value).
* `async def` with an `await` becomes a coroutine while `async def` with `yield` becomes an asynchronous generator.
* `async for` can be used for iterating over async generators.
* To get the return value of a coroutine (`async def...await`), the caller has to await on that coroutine.
* `async with` can be only used inside a coroutine `async def`. Asynchronous context managers define `__aenter__` and `__aexit__` methods.
* `await` can be used only on an **awaitable**. An awaitable is either a coroutine or an object that implements `__await__` that returns an iterator.

## Async IO design patterns

* Coroutines can be chained.

```Python
async def corot1(*args):
    # contains some awaitable stuff like
    # network call
    pass

async def corot2(*args):
    # awaits on some HTTP call
    pass

async def wrapper_corot(*args):
    r1 = await corot1(*args)
    print(r)
    r2 = await corot2(*args)
    return (r1, r2)

async def async_driver():
    await asyncio.gather([
        wrapper_corot(1,2,3),
        wrapper_corot(4,5,6),
        wrapper_corot(7,8,9)])
```

* `asyncio.Queues` can be used as a transparent way of communication between the producers and consumers. Consumer will be blocked on `asycio.Queue.get` method and the producer will be awaiting on the `asyncio.Queue.put` operation if the queue is full.

## `async for` and asynchronous comprehensions

* Used with asynchronous generator(iterator). At each iteration, we will be invoking some asynchronous operation.

> All that they do is provide the look-and-feel of their synchronous counterparts, but with the ability for the loop in question to give up control to the event loop for some other coroutine to run.

```Python
# async generators
async def mygen(b, n):
    i = 0
    while i < n:
        print("Yielding a value")
        yield b ** i
        i += 1
        # Here the task will give the control to event loop
        await asyncio.sleep(1)
        print("Back after sleeping")

# async for indicates that after calling the next on the
# async generator, CPU control will be given back to the event loop
# because the generator goes into await on some IO
async def async_driver():
    # async comprehensions
    g = [i async for i in mygen(2,10)]

    # async for
    async for j in mygen(3, 5):
        print(j)
    return g

asyncio.run(async_driver())
```

## Event loop

> `asyncio.run()`, introduced in Python 3.7, is responsible for getting the event loop, running tasks until they are marked as complete, and then closing the event loop.

* Orchestrates the execution of coroutines. Event loop is single threaded.

* Custom implementations of event loop is allowed. [uvloop](https://github.com/MagicStack/uvloop) package provides one such custom implementation.

* To run event loop in multiple CPUs, [refer to this talk](https://youtu.be/0kXaLh8Fz3k?t=10m30s)

## Asyncio alternative packages

* [curio](https://github.com/dabeaz/curio)
* [trio](https://github.com/python-trio/trio)

## Top level asyncio functions

* (Python 3.7+)`asyncio.create_task(coroutine)` - Schedule the execution of a coroutine object. `asyncio.run(main_coroutine)` triggers the execution.
* (Python 3.6) `asyncio.ensure_future()` - behaves the same as `asyncio.create_task()`
* `asyncio.Task.all_tasks()` - returns all the pending tasks.
* `asyncio.gather(coroutines_or_futures)` - `gather()` is meant to put a **collection of coroutines(futures)**  into a single future. If you `await asyncio.gather()` on multiple tasks or coroutines, you’re waiting for all of them to be completed. The result of `gather()` will be a list of the results across the inputs.

* `asyncio.as_completed()` - to get tasks as they are completed, in the order of completion.

```Python
import asyncio

async def async_coroutine(id):
    await asyncio.sleep(1)
    print(f"Inside coroutine with id:{id}")
    return id

async def main():
    task1 = asyncio.create_task(async_coroutine(1))
    task2 = asyncio.create_task(async_coroutine(2))
    print(futures)
    # as_completed returns an iterator of coroutines.
    # we will get the results in the order in which the coroutines complete
    for async_task in asyncio.as_completed([task1, task2]):
        result = await async_task
        print(f"Task result: {result}")

    print(all([task1.done(), task2.done()]))

asyncio.run(main())
```

---

## References

* [Python asyncio package docs](https://docs.python.org/3/library/asyncio.html)
* [Python async features](https://realpython.com/python-async-features/)
* [Async IO in Python](https://realpython.com/async-io-python/)

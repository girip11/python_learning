# Asyncio Coroutines and tasks

* If the code execution is currently happening inside an `async def` function, then there exists an event loop in the current thread which can be obtained using `asyncio.get_running_loop()`.

## Coroutine

```Python
import asyncio

# `main` is a coroutine function
# Calling a coroutine function returns a coroutine object
# but the coroutine function body is not executed.
async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# we get a coroutine object
corout_obj = main()

asyncio.run(corout_obj)
# or
asyncio.run(main())
```

## Executing a coroutine

* Using `asyncio.run(<coroutine_obj>)` to trigger the execution of a coroutine.

* `await` on a coroutine from inside another coroutine, schedules the coroutine object for execution.

```Python
import asyncio

async def print_msg(id, msg):
    print(f"Coroutine-{id}: Entered print_msg")
    await asyncio.sleep(1)
    print(f"Coroutine-{id}:{msg}")
    print(f"Coroutine-{id}: Exited print_msg")

# main() returns a coroutine
async def main():
    # main() execution gets blocked here. Only when the first coroutine
    # completes, the next statement gets executed.
    await print_msg(1, "Hello world")
    await print_msg(2, "Foo bar")

async def concurrent_main()
    # In this case both the coroutines are executed concurrently
    await asyncio.gather(print_msg(1, "Hello world"), print_msg(2, "Foo bar"))

# Output
# Coroutine-1: Entered print_msg
# Coroutine-1:Hello world
# Coroutine-1: Exited print_msg
# Coroutine-2: Entered print_msg
# Coroutine-2:Foo bar
# Coroutine-2: Exited print_msg
asyncio.run(main())

# OUTPUT
# Coroutine-1: Entered print_msg
# Coroutine-2: Entered print_msg
# Coroutine-1:Hello world
# Coroutine-1: Exited print_msg
# Coroutine-2:Foo bar
# Coroutine-2: Exited print_msg
asyncio.run(concurrent_main())
```

* Creating an async task `asyncio.create_task(coroutine_obj)` and awaiting on that task from a coroutine. **Executing coroutines via tasks makes the coroutines execute concurrently.**

* Calling a coroutine function returns a coroutine object. That coroutine object is not given to event loop automatically for it to be scheduled to run. **Awaiting on a coroutine object makes it schedulable by event loop.**

* Creating a task out of a coroutine object, places the coroutine object in the event loop and is scheduled to run automatically when the caller coroutine enters awaiting state.

```Python
import asyncio

async def print_msg(task_id, msg, wait_time):
    print(f"Task-{task_id}: Entered print_msg")
    await asyncio.sleep(wait_time)
    print(f"Task-{task_id}:{msg}")
    print(f"Task-{task_id}: Exited print_msg")

# main() returns a coroutine
async def main():
    # Now event loop will have 2 coroutine objects ready to run as
    # soon as this main coroutine gets blocked(await)
    task1 = asyncio.create_task(print_msg(1, "Hello world", 3))
    task2 = asyncio.create_task(print_msg(2, "Foo bar", 1))

    # control is not blocked after creating tasks
    print("Still the control is with the main coroutine")
    # lets print all the pending tasks in the event loop
    # This should print 3 tasks task1, task2 and main()
    print(f"{asyncio.all_tasks()}")

    # now main() coroutine will relinquish CPU and next task1
    # is in event loop
    # Since task1 is waiting for 3 seconds and task2 is waiting for 1 second
    # task2 completes before the task1.
    # When the control reaches here, task1 and task2 would have been completed
    await task1
    print("Task1 is completed")
    await task2
    print("All tasks complete")

# Output
# Still the control is with the main coroutine
# {<Task pending coro=<print_msg(),
#  <Task pending coro=<print_msg(),
#  <Task pending coro=<main() }
# Task-1: Entered print_msg
# Task-2: Entered print_msg
# Task-2:Foo bar
# Task-2: Exited print_msg
# Task-1:Hello world
# Task-1: Exited print_msg
# Task1 is completed
# All tasks complete

asyncio.run(main())
```

## Awaitable objects

* Objects that can be used in `await` expression are **awaitable objects**.
* `Task`, `Future` and `coroutine` are awaitable objects.

## [Tasks](https://docs.python.org/3/library/asyncio-task.html#task-object)

> Tasks are used to schedule coroutines concurrently.

* A task object wraps a coroutine object.

* Execution happens concurrently along with the coroutine that created the task. Only when the coroutine that created the tasks relinquishes CPU by notifying the event loop(awaiting on something notifies event loop), created tasks will be able to run.

```Python
import time

async def blocking_main():
    # task will execute concurrently with main
    # (i.e) when main() awaits on something
    # task gets a chance to run
    task = asyncio.create_task(print_msg(1, "Blocking"))
    # This is a blocking sleep, only when main
    # wakes from this sleep the task will run
    # since we await on the task
    time.sleep(10)
    print("Task execution will begin on await task")
    await task
    print(task.result())
    print(task.done())

async def concurrent_main():
    # task will run as soon as main coroutine awaits
    task = asyncio.create_task(print_msg(2, "Concurrent"))
    # Sleep more than the task sleep time
    await asyncio.sleep(3)
    print("This will get printed after the task execution is complete since task sleeps for 1 second only")
    await task
    print(task.result())
    print(task.done())
```

## Future

> * A `Future` is a **special low-level awaitable object** that represents an eventual result of an asynchronous operation
> * When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.

```Python
async def main():
    # function can be some asyncio library function that returns a
    # Future
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
```

## Running an asyncio program (needs python 3.7+)

* `asyncio.run` always creates a new event loop and manages it internally. Should ideally be called once. **This function cannot be called when another asyncio event loop is running in the "same thread"**.

* `asyncio.create_task(coro, *, name=None)` schedules the coroutine to run in the event loop in the current thread. Remember we can have only 1 event loop in 1 thread.

## Asyncio functions

**NOTE** - Ignore the loop parameter in all these functions as they are deprecated.

* `asyncio.sleep(delay, result=None, *, loop=None)`

* `asyncio.gather(*aws, loop=None, return_exceptions=False)` - Run all the awaitables concurrently. If `return_exceptions=True`, exceptions are also returned as results, if `False` exception raised to coroutine that awaits `gather()`. Results follow same order of awaitables in **aws**. We can safely cancel a task among many tasks given to `gather()`.

> If the gather itself is cancelled, the cancellation is propagated regardless of return_exceptions.

* `asyncio.shield(aw, *, loop=None)` - Protect an awaitable object from being cancelled externally. If the awaitable is cancelled from itself, that would cancel shield.

* `asyncio.wait_for(aw, timeout, *, loop=None)` - Wait for the awaitable to complete within a timeout. If a timeout occurs, it cancels the task and then raises `asyncio.TimeoutError`. If the wait is cancelled, awaitable `aw` is also cancelled.

* `asyncio.wait(aws, *, loop=None, timeout=None, return_when=ALL_COMPLETED)` - This method returns a 2-tuple `(done_tasks_objects, pending_task_objects)`. No exception raised on timeout as well as no tasks are cancelled. `return_when` values are `FIRST_COMPLETED`, `FIRST_EXCEPTION`, `ALL_COMPLETED`

```Python
done, pending = await asyncio.wait(aws)
```

* `asyncio.as_completed(aws, *, loop=None, timeout=None)` - Return an iterator of coroutine objects which can be awaited to get the **earliest result**. Raises `asyncio.TimeoutError` if the timeout happens.

```Python
async def random_wait(t):
    await asyncio.sleep(t)
    return t

async def main():
    for cor in asyncio.as_completed([random_wait(3), random_wait(1)]):
        earliest_result = await cor
        print(earliest_result)

# output will be in the order of coroutine completion
# and not in the order that we gave to as_completed method
# OUTPUT
# 1
# 3
asyncio.run(main())
```

* `asyncio.run_coroutine_threadsafe(coro, loop)->concurrent.futures.Future` - Schedules the coroutine to run on a different event loop on different thread.
* `asyncio.get_running_loop()` returns the event loop in the current thread.
* `asyncio.current_task(loop=None)` - get the current running task on given event loop. If event loop is `None`, it is obtained from `get_running_loop`.
* `asyncio.all_tasks(loop=None)` - Returns set of unfinished tasks in the input event loop.

---

## References

* [Asyncio Coroutines and tasks](https://docs.python.org/3/library/asyncio-task.html)
* [Asyncio exceptions](https://docs.python.org/3/library/asyncio-exceptions.html)

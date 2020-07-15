# Asyncio Synchronization primitives

* `Lock`, `Event`, `Condition`, `Semaphore` and `BoundedSemaphore`
* These primitives are not thread safe.
* These primitives can be created inside coroutines only. Creating in code outside of event loop raises `RuntimeError`

## Lock

* Task that holds the lock will be able to enter the context manager block

```Python
import asyncio

mutex_lock = asyncio.Lock()

async with mutex_lock:
    # exclusive access to the shared resource
```

* Entering the context manager is possible only after acquiring the lock and the lock is automatically released once the context manager is exited.

## Event

* Event is used to notify multiple tasks that some event has happened.

```Python
import asyncio

async def waiters(event):
    # tasks will wait on wait() method
    print("Waiting")
    await event.wait()
    # logic
    print("Received event")

async def signal(event):
    # do something and then set the event
    await asyncio.sleep(2)
    print("Signalling the event")
    event.set()

async def main():
    event = asyncio.Event()
    tasks = [asyncio.create_task(waiters(event)) for i in range(5)]

    # this await will make all waiters to be blocked
    await signal(event)
    print("Event signalled")
    # Wait till all waiters get executed
    await asyncio.gather(*tasks)

asyncio.run(main())
```

## Condition

* This combines the functionality of lock and event.
* Tasks who acquire the lock inside the condition object can notify one or all other tasks blocked on this condition.
* When tasks inside the condition lock call `wait` or `wait_for` they release the lock and get blocked.

```Python
import asyncio

async def waiters(cond):
    # tasks will wait on wait() method
    print("Waiting")
    async with cond:
        await cond.wait() # lock will be released
    # logic
    print("Condition successful")

async def signal(cond):
    # do something and then set the condition to notify all
    await asyncio.sleep(2)
    async with cond:
        print("Notifying the waiters")
        cond.notify_all()

async def main():
    cond = asyncio.Condition()
    tasks = [asyncio.create_task(waiters(cond)) for i in range(5)]

    # this await will make all waiters to be blocked
    await signal(cond)
    # Wait till all waiters get executed
    await asyncio.gather(*tasks)

asyncio.run(main())
```

## Semaphore

* Allows n tasks to share a resource. `acquire()` decrements the counter and `release()` increments the counter.

```Python
sem = asyncio.Semaphore(10)

# This semaphore can be passed to all coroutines and
# those can acquire this and work on the shared resource.
async with sem:
    # work with shared resource
```

* Any number of calls to `release()` method is allowed.
* Suppose I want only 100 coroutines to run concurrently, then I can create a semaphore of value 100 and thus I can limit the concurrency.

## Bounded semaphore

* `asyncio.BoundedSemaphore(value=1, *, loop=None)` In bounded semaphore, when the internal counter exceeds the initial value, exception is raised.

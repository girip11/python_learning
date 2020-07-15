# Asyncio Queues

* `asyncio.Queue` help in exchange of data between asyncio tasks.
* This queue is not thread safe.

## `asyncio.Queue` methods

* `asyncio.Queue(maxsize=0, *, loop=None)` - If maxsize < 0, then queue's capacity is infinite.
* `maxsize`, `qsize()`, `empty()`, `full()` - Queue size related methods.

### Async methods

* `coroutine get()` - get an item from the queue. Block if the queue is empty.
* `coroutine put()` - add an item to the queue. Block if the queue is full.
* `coroutine join()` - Block till all items in the queue are received and processed. Each consumer task calls `Queue.task_done()` after it processes the item it got from the queue. When`task_done` is called for all items that were put into the queue, join unblocks.

* `get_nowait()` and `put_nowait()` - get from or put to the queue without blocking. Raises exception when queue is either empty(`QueueEmpty`) or full(`QueueFull`).

## Other queues

* `asyncio.PriorityQueue` - each entry is a `tuple(priority, item)`. Get will always fetch the item of highest priority.
* `asyncio.LifoQueue` - Last in first out. `get` will fetch the most recently added item from this queue.

---

## References

* [Asyncio queues](https://docs.python.org/3/library/asyncio-queue.html)

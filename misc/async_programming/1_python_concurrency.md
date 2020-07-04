# Concurrency in python

* Concurrency - run on single core with preemptive (or cooperative) multitasking, giving the illusion of running simulataneously.
* Parallelism - run on multi cores

* Notes on [Concurrency vs Parallelism](https://bitbucket.org/girip11/cs_learnings/src/master/processors_threads_cores/multiprocessing_multithreading.md)

* Notes on multiCPUs, multicores, hyperthreading[Concurrency vs Parallelism](https://bitbucket.org/girip11/cs_learnings/src/master/processors_threads_cores/multicpu_multicores_hyperthreading.md)

Concurrency and parallelism can be achieved in python using `threading`, `multiprocessing` and `asyncio` packages.

## Using threads

* Using `threading` package, we can create new threads and the OS can switch between these threads based on time slice. This is **preemptive multitasking**.
* With multiple threads, each thread can be run on different core/CPU. But that's not the case in python. Due to Global Interpreter Lock(GIL), even if a process has many threads, the thread that has the GIL can run.
* In python at any point in time only a single threads runs, but we get the illusion of multiple threads running at the same time by quickly context switching between these threads.

## Using asyncio

* In asyncio, we deal with tasks. All tasks will run on the same thread and there is a single thread only.
* Python maintains an event loop that tracks all the tasks. A task will be context switched only when its blocked for IO or gets completed. This is **cooperative multitasking**.
* This is very suitable if we have lots of tasks that need to perform IO operations. As soon as a task gets blocked waiting for an IO to complete, next task in the event loop gets loaded.

* Useful in running IO bound workloads. (Speeding it up involves overlapping the times spent waiting for these devices.)

## Using multiprocessing

* Multiprocessing in python is achieved by spawning multiple sub processes which can run on each CPU independently. Thus true parallelism is achieved using multiprocessing in python.

* Speeding up of CPU bound operations involves finding ways to do more computations in the same amount of time. This can be helpful in running CPU bound operations in parallel.

* Concurrency code snippets for reading file can be found in [concurrency snippets](./../../tryouts/concurrency/)

---

## References

* [Python concurrency](https://realpython.com/python-concurrency/)

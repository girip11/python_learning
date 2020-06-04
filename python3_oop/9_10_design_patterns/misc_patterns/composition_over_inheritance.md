# Composition over inheritance

> Favor object composition over class inheritance. - GOF

Consider the following logger customization problem.

* Filter log messages based on a pattern.
* Provision to write the log to file or socket or syslog or to all.

## Design based on inheritance

* Subclass explosion (m * n)

```text
Logger            FilteredLogger
SocketLogger      FilteredSocketLogger
SyslogLogger      FilteredSyslogLogger
```

## Redesigning above problem using adapter pattern

* Logger expects a file like object to write to.
* Using duck typing, we can write adapters that interface between a file and a socket, and another one interfacing between a file and syslog.

```text
Logger(FileLikeObject)
FilteredLogger(FileLikeObject)

File
FileSocketAdapter
FileSyslogAdapter
```

* Depending on the medium to which the logs should be sent to and whether they have to be filtered or not, we can choose the logger class and the adapter class.

## Redesigning using the bridge pattern

Another way to solve this problem is to use the bridge pattern, where we separate the logger interface from the implementation of where the log is written to.

```text
Client -->      Logger(handler)             -> FileHandler(file)
                FilteredLogger(handler)     -> SocketHandler(socket)
                                            -> SyslogHandler(syslog)
```

## Redesigning using the decorator pattern

Both the above solutions lack symmetry/ recursive composition. If filter pattern2 needs to be applied to another filter logger with pattern1, its easier to design using the decorator pattern.

```text
FileLogger
SocketLogger
SyslogLogger
<!-- This decorator can accept one of above objects -->
FilteredLogger(anotherLogger)
```

Here we pivot the initial classes around the medium to which we need to log the messages. Then we enhance their interface like filtering using additional decorators.

* While the decorators can be stacked, we can target writing log only to a single medium.

## Python's logging module solution

> Python’s logging module wanted even more flexibility: not only to support multiple filters, but to support multiple outputs for a single stream of log messages.
> The Python logging module implements its own Composition Over Inheritance pattern.

```Python
class Logger:
    def __init__(self, filters, handlers):
        self.filters = filters
        self.handlers = handlers
```

* This solution seems to be highly cohesive in terms of writing filters and handlers.

> There’s a crucial lesson here: design principles like Composition Over Inheritance are, in the end, more important than individual patterns like the Adapter or Decorator. Always follow the principle. But don’t always feel constrained to choose a pattern from an official list. The design at which we’ve now arrived is both more flexible and easier to maintain than any of the previous designs, even though they were based on official Gang of Four patterns but this final design is not. Sometimes, yes, you will find an existing Design Pattern that’s a perfect fit for your problem — but if not, your design might be stronger if you move beyond them.

Following this, this article very nicely explains what kind of solutions should be avoided while designing the above problem.

* Dodge(avoid) if statements
* Dodge multiple inheritance
* Dodge mixins
* Dodge building classes dynamically

---

## References

* [The Composition Over Inheritance Principle](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)

<!-- Saved the article in pocket: https://app.getpocket.com/read/2949881456 -->

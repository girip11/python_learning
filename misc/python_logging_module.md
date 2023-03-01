# Python's builtin logging module

**NOTE**: Methods in this module follow camelCasing instead of the usual snake casing.

## Using default logger

```Python
import logging

logging.debug("This is a debug log")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")
```

- By default the root logging's level is set to warning. So the DEBUG and INFO level won't show up.

- By default the root logger logs to the console.

- The log levels are available as constants in the logging module. Ex - `logging.DEBUG`

### Customizing the default logger

- `logging.basicConfig()` method can be called to customize the root logger with custom handlers, logging level, log message format, datetime format etc.
- Before python 3.8, the `basicConfig` of the root logger can be called only once. In python 3.8, `force` parameter was added to the `basicConfig` to overwrite the existing configuration.

#### Change logging level

```Python
import logging

logging.info("This is an info log. It will not be seen on console.")
logging.basicConfig(level=logging.INFO, force=True)
logging.info("This is an info log. It will now be seen on console.")
```

**NOTE** - Calling any of the `debug`, `info`, `warning`, `error`, `critical` methods on the logging module will call `basicConfig()` implicitly. Therefore from python 3.8 onwards, we can ensure this by setting the `logging.basicConfig(level=logging.INFO, force=True)`. This will apply the configuration forcefully.

#### Changing logging format

- [All attributes of the `LogRecord`](https://docs.python.org/3/library/logging.html#logrecord-attributes) can be used in the format string. `help(logging.Formatter` gives you nice documentation of all the attributes that can be used in the format string.

- For configuring datetime format, we can use the [format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) used for `time.strftime`

```Python
import logging

logging.basicConfig(level=logging.INFO,
format="%(asctime)s - %(process)d - %(levelname)s - %(message)s",
datetime="%d-%m-%y_%H:%M:%S")

logging.info("Hello")
```

### Logging Exceptions

- Calling `logging.exception()` inside `except` block will log the exception with `ERROR` severity.
- To log an exception with severity other than error we need to pass `exc_info=True` to the method that we want to log, ex-`logging.critical("Critical error", exc_info=True)`

```Python
try:
    num = 1
    den = 0
    print(num/den)
except ArithmeticError as e:
    logging.exception("Unable to perform division")
    # logging the exception as warning
    logging.warning("Unable to perform division", exc_info=True)
```

## Create new Loggers

- `logging.getLogger(name)` returns a new instance of the `Logger` class. If an instance exists in the same python interpreter process with the given name, existing instance is returned.

- Instances of `Logger` can be customized using handlers and formatters.

> It is recommended that we use module-level loggers by passing `__name__` as the name parameter to getLogger() to create a logger object as the name of the logger itself would tell us from where the events are being logged. `__name__` is a special built-in variable in Python which evaluates to the name of the current module. - [Logger python doc](https://docs.python.org/3/library/logging.html#logger-objects)

- Each logger instance can have several handlers and filters.

```Python
import logging

logger = logging.getLogger(__name__)

print(logger.isEnabledFor(logging.INFO))

logger.getEffectiveLevel()

logger.setLevel(logging.WARNING)

logger.warning("This is a warning")
```

## Using Handlers

- A logger can have several handlers each with its own severity level. `Handler.setLevel()` is called to set the logging level for that handler instance.

- Also each handler can be passed an instance of the formatter. `Handler.setFormatter()` is called to set the formatter on the handler.

- `Logger.addHandler()` is used to add handlers to the logger instance.

- There are several builtin handlers provided by the `logging` module.

```Python
import logging
import sys
logger = logging.getLogger(__name__)

# create handlers
stdout_handler = logging.StreamHandler(stream=sys.stdout)
stdout_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.ERROR)

# create formatters
# we can specify the message format and the dateformat
stdout_formatter = logging.Formatter("%(process)s-%(levelname)-%(message)s")
file_formatter = logging.Formatter("%(asctime)s-%(message)s", datefmt="%d-%m-%y_%H:%M:%S")

# add formatters to the respective handlers
stdout_handler.setFormatter(stdout_formatter)
file_handler.setFormatter(file_formatter)

# add the handlers to the logger instance
logger.addHandler(stdout_handler)
logger.addHandler(file_handler)

# This message will be logged to console as well as the file
logger.error("This is an error")
```

## Adding filters to Logger

- By setting logging level, we can filter out the log records. But if we want to do filtering by the message content or some preprocessing like counting the logs containing some keyword, we use create custom filters and add them to the loggers.

- `Logger.addFilter()` accepts the following

  - a callable that accepts `Logrecord` as its parameter and returns either 0(reject) or nonzero(allow).
  - Instance of a type that is a subclass of `logging.Filter`
  - Any object that implements the `filter` method(duck typing)

- `LogRecord` has the following useful attributes: `'args', 'exc_info', 'exc_text', 'filename', 'funcName', 'levelname', 'levelno', 'lineno', 'module', 'msecs', 'msg', 'name', 'pathname', 'process', 'processName', 'relativeCreated', 'stack_info', 'thread', 'threadName'`

```Python
import logging

def drop_lengthy_messages(record):
    return 1 if len(record.msg) <= 50 else 0

class LogCounter(logging.Filter):
    def __init__(self, *args, **kwargs):
        self.count = 0
        super().__init__(*args, **kwargs)
    def filter(self, record):
        self.count += 1
        return 1

logger = logging.getLogger("test")
logger.setLevel(logging.INFO)
logger.addFilter(drop_lengthy_messages)

log_counter = LogCounter()
logger.addFilter(log_counter)

logger.info("hello")

print(log_counter.count)
```

## Other ways to configure logger

- Configuration file using `logging.config.fileConfig(fname)`

```Conf
[loggers]
keys=root,sampleLogger

[handlers]
keys=consoleHandler

[formatters]
keys=sampleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_sampleLogger]
level=DEBUG
handlers=consoleHandler
qualname=sampleLogger
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=sampleFormatter
args=(sys.stdout,)

[formatter_sampleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
```

- Using `logging.config.dictConfig` which can be useful when logging configuration is in YAML format.

## Child loggers

- When we want to apply a package hierarchy for loggers, we can create a parent logger in the parent package, and create many child loggers for different subpackages/modules inside them.
- Only the parent logger is configurable. Child loggers cannot be configured.

- To create a child logger we could either use `parent_logger.getChild(child_name_only)` or `logging.getLogger(f"{parent_logger_name_prefix}.{child_logger_name}")`

```Python
import logging

parent = logging.getLogger("parent")
print(parent.name)

# This would return a logger names parent.child
child = parent.getChild("child")
print(child.name)
```

---

## References

- [Logging python documentation](https://docs.python.org/3/library/logging.html#logrecord-attributes)
- [Logging in Python](https://realpython.com/python-logging/)

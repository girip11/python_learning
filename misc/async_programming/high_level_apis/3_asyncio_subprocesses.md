# Subprocesses

## Subprocess creation API

Below APIs return the `Process` object.

* `asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None, loop=None, limit=None, **kwds)` - creates a  subprocess to run the shell command
* `asyncio.create_subprocess_exec(program, *args, stdin=None, stdout=None, stderr=None, loop=None, limit=None, **kwds)` - creates a subprocess to run the program

* If parent and child processes need to communicate with each other, we need to set stdin, stdout, stderr to `asyncio.subprocess.PIPE`. With this parent can send input to child as well as read the stdout and stderr contents of the child process.

* To redirect stderr to stdout, use `asyncio.subprocess.STDOUT`.

* Another constant `asyncio.subprocess.DEVNULL` can also be set for stdin, stdout and stderr.

## `Process` object

* `wait()` - coroutine function waits till the child process terminates. If we need to wait till a timeout, we can use `asyncio.wait_for(awaitable_obj, timeout)`

* `communicate(input)` - This is recommended when stdin, stdout and stderr are set to `asyncio.subprocess.PIPE`. This coroutine function returns a tuple(reader, writer)

* `send_signal(signal)`, `terminate()`, `kill()` - can be used to send signal or to kill the child process.

* Child process exit code available from `returncode` and `pid` contains the child process id

* `stdin(StreamWriter)`, `stdout(StreamReader)` and `stderr(StreamReader)` attributes are available to asynchronously read and write to and from the child process. This is used when the child process was created with `asyncio.subprocess.PIPE` as stdin, stdout and stderr.

```Python
import asyncio
from typing import List

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

async def main(commands: List[str]):
    tasks = [asyncio.create_task(run(cmd)) for cmd in commands]
    await asyncio.gather(*tasks)

asyncio.run(main(
    ['python --version', 'java -version', 'scala -version']))
```

* Example using `create_subprocess_exec`.

```Python
import asyncio
import sys
from typing import List

async def run(python_code: str):
    proc = await asyncio.create_subprocess_exec(
        sys.executable,
        '-c',
        python_code,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    print(f"Executing {sys.executable}")
    stdout, stderr = await proc.communicate()
    if stdout:
        return stdout.decode()
    if stderr:
        return stderr.decode()

async def main(snippets: List[str]):
    tasks = [asyncio.create_task(run(snippet)) for snippet in snippets]

    for task in asyncio.as_completed(tasks):
        task_output = await task
        print(f'[OUTPUT]\n{task_output}')


asyncio.run(main(
    [
"""import datetime
import time
time.sleep(2)
print(datetime.datetime.now())
""",
"""import random
import time
time.sleep(2)
print(random.randint(1, 100))
""",
"""
# This will raise error
print("Hello" + 5)
"""
    ]))
```

---

## References

* [Async apis to create and manage subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html)

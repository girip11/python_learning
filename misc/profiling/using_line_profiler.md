# Using line profiler

> The current profiling tools supported in Python only time function calls. This is a good first step for locating hotspots in one's program and is frequently all one needs to do to optimize the program. However, sometimes the cause of the hotspot is actually a single line in the function, and that line may not be obvious from just reading the source code. These cases are particularly frequent in scientific computing. Functions tend to be larger (sometimes because of legitimate algorithmic complexity, sometimes because the programmer is still trying to write FORTRAN code), and a single statement without function calls can trigger lots of computation when using libraries like numpy. cProfile only times explicit function calls, not special methods called because of syntax.
>
> LineProfiler can be given functions to profile, and it will time the execution of each individual line inside those functions. In a typical workflow, one only cares about line timings of a few functions because wading through the results of timing every single line of code would be overwhelming. However, LineProfiler does need to be explicitly told what functions to profile.

Line profiler is written in Cython to reduce the profiling overhead.

## Usage

- Functions can be decorated with `@profile`.

```bash
# profile a python script
kernprof -lv python_script.py
```

Results of the profiler are stored in a file named `python_script.py.lprof` using the binary format.

To view the file `python -m line_profiler <python_script.py.lprof>` is used.

## Explicit invocation

```python
import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)

@profile
def is_addable(l, t):
    for i, n in enumerate(l):
        for m in l[i:]:
            if n + m == t:
                return True

    return False

assert is_addable(range(20), 25) == True
```

If you want to profile several functions, only instantiate once the `LineProfiler` and import it in the other files. If you don’t do that, you might have some issues and weird reporting.

---

## References

- [line_profiler](https://github.com/pyutils/line_profiler)
- [Profiling python code line by line](https://towardsdatascience.com/a-quick-and-easy-guide-to-code-profiling-in-python-58c0ed7e602b)
- [Use line_profiler without magic](https://lothiraldan.github.io/2018-02-18-python-line-profiler-without-magic/)
- [Line profiling of python code](https://coderzcolumn.com/tutorials/python/line-profiler-line-by-line-profiling-of-python-code)

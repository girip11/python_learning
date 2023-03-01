# Using `cProfile` module

## Using `cProfile` and `pstats` modules

To profile a python script from command line, use the following command

```bash
# sort_order options are
# https://docs.python.org/3/library/profile.html#pstats.Stats.sort_stats
python -m cProfile script_to_profile.py -o profiled_stats [-s sort_order]
```

## Profiling by writing python code

```python
import cProfile
cProfile.run(statement="print('Hello world')")
```

```python
import cProfile
import pstats

# Using this we can only profile a section of the code we are interested in
profiler = cProfile.Profile()
profiler.enable()
say_hello(name)
profiler.disable()

profiled_stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE)
profiled_stats.print_stats()
```

---

## References

- [The Python Profilers](https://docs.python.org/3/library/profile.html)
- [Profiling python code](https://machinelearningmastery.com/profiling-python-code/)
- [Profiling Python with valgrind](https://thomas-cokelaer.info/blog/2013/10/profiling-python-with-valgrind/)

import cProfile
import pstats
from pathlib import Path

# import re  # noqa


def say_hello(name: str) -> None:
    print(f"Hello {name}")

cProfile.run(statement="say_hello('John')")

# cProfile.run(statement="re.compile('foo|bar')")

name="Jane"
# visualize the result with tuna
cProfile.runctx(statement="say_hello(name)", 
                globals=globals(), 
                locals=locals(), 
                filename=f"{Path(__file__).parent}/test_profiling_stats.prof")

# This is a way to profile part of the code
profiler = cProfile.Profile()
profiler.enable()
say_hello(name)
profiler.disable()

profiled_stats = pstats.Stats(profiler).strip_dirs().sort_stats(pstats.SortKey.CUMULATIVE)
profiled_stats.print_stats()

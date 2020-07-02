# Python Modules

* A python file(.py) is a module. It can contain methods, classes etc. Name of the module is the name of the python file, except the name of the main module is always "__main__"

* A python package is a directory containing python modules and additionally `__init__.py` file.

* Each module has its own private symbol table, and importing a module adds the names in the module to the importing module's global symbol table.

* A module is executed the first time its imported

## Importing modules using `import` statement

* `import <module_name>` - When import is used alone, it can import a python module (as well as a package).

* Access names in the imported module with **the imported name** followed by the dot operator and then the name.

```Python
# from sys builtin  module
import sys
print(sys.modules)

# from python random module random.py
import random
dir(random.Random)

# A module can be imported at any point in the code uisng the plain import statement
def get_random_int(min, max):
    import random
    return random.Random().randint(min, max)

get_random_int(10, 100)
```

### Importing modules using `from .. import` statement

* `from <module> import <object>` - From a package or a module we can import a subpackage or a module or an object like class or function.

```Python
# from sys builtin  module
from sys import argv
for arg in argv:
    print(arg)

from random import Random
print(Random().randint(10, 100))

def get_random_int(min, max):
    from random import Random
    return Random().randint(min, max)

get_random_int(10, 100)
```

* Alias can be assigned to the imported object using `as` to avoid any name collision

```Python
# aliasing using as
from sys import argv as cmdline_args
for arg in cmdline_args:
    print(arg)
```

### Importing using wildcard `*`

* Not a recommended approach. Imports all names under a module or a package.
* Can lead to name collision Always recommended to explicitly import what is required.

**NOTE**: * Wildcard import statements can only be used at module level.

```Python
from random import *
print(Random().randint(10, 100))

# This type of import cannot be used inside functions and classes.
def get_random_int(min, max):
    from random import *
    return Random().randint(min, max)

# On execution raises SyntaxError
# SyntaxError: import * only allowed at module level
get_random_int(10, 100)
```

### Dynamically importing modules using `__import__`

```Python
#  __import__ helps in dynamic import during runtime.
import re as regex
regex = __import__('re')

# info on __import__
help(__import__)

# runtime module import
module_name = 'random'
random_gen = __import__(module_name)
```

## Structuring modules

* Good practice to have **all the imports at the top**.

* Recommended to order python modules in to the following groups
  * Builtin modules and python library modules arranged alphabetically
  * Third party python packages arranged alphabetically
  * Imports from the packages within the project arranges alphabetically.

* Module variables/classes with leading underscore are treated internal to the module and are not imported to other modules when using wildcard import `from module import *`. But **explicit import is allowed**.

## `__name__` variable

Used when module is executed on its own like a python script.

```Python
# module variables

# module methods

# module classes etc

# condition is True when the module is executed on its own
if __name__ == "__main__"
    # module execution code
    from sys import argv
    # use the argv commadline arguments

```

## Reload module changes dynamically

Using the python module **imp**. Module reloads are **additive**. For instance, add a method, rename the method, after the module reloads we will find both the methods available.

```Python
import my_module
import importlib

dir(importlib)

# after changes in my_module
importlib.reload(my_module) # reload the changed module.
```

## Module search path

* First python interpreter searches in `sys.modules`(modules cache) to see if the module is imported already.

```Python
import sys

print(sys.modules)
# first time importing a package, it executes __init__.py
# first time loading a module, executes the module
import tryouts.simple_package

print(sys.modules)
# Second time no import will happen, since the entry is already found in the
# sys.modules
import tryouts.simple_package
```

* If the module is not imported already, then the python interpreter does the following to load the module.

> When a module named `spam` is imported, the interpreter first searches for a **built-in module** with that name. If not found, it then searches for a file named `spam.py` in a list of directories given by the variable `sys.path`
> The variable `sys.path` is a list of strings that determines the interpreter’s search path for modules. `sys.path` is initialized from these locations:
>
> * The directory containing the input script (or the current directory when no file is specified).
> * PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
> * The installation-dependent default.
>
> The directory containing the script being run is placed at the beginning of the search path, ahead of the standard library path

```Python
import sys

# lists all the search locations of python interpreter to find a package or module
print(sys.path)

print(type(sys.path))

# sys.path.append("")

# To list all the loaded modules
print(sys.modules)
```

> Built-in modules are written in C and integrated with the Python interpreter. Each built-in module contains resources for certain system-specific functionalities such as OS management, disk IO, etc. The standard library also contains many Python scripts (with the .py extension) containing useful utilities. - [Builtin module vs standard library modules](https://www.tutorialsteacher.com/python/python-builtin-modules)

* Module compiled to byte code and saved in **.pyc** file to avoid recompilation. Bytecode is platform independent.

---

## References

* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)

* [Python3 modules](https://docs.python.org/3/tutorial/modules.html)

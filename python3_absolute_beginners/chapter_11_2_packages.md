# Modules and Packages

* A python package is a directory containing python modules and additionally `__init__.py` file

* The `__init__.py` files are required to make Python treat directories containing the file as **packages**.

* When you import a package, it runs the `__init__.py` file inside the package directory. `__init__.py` is a normal python file that can contain usual python constructs like class, conditional constructs etc.

* When you execute a package (e.g. `python -m my_package`) it executes the `__main__.py` file.

> When importing the package, Python searches through the directories on `sys.path` looking for the package subdirectory.
> Note that relative imports are based on the name of the current module.Since the name of the main module is always `__main__`, modules intended for use as the main module of a Python application **must always use absolute imports**. - [Modules and Packages](https://docs.python.org/3/tutorial/modules.html)

## Importing packages and modules

### Importing packages and modules using `import` statement

* `import <package | module >` - When import is used alone, it can import a python module or a package.

* Access names in the imported module with **the imported name** followed by the dot operator and then the name.

> When using syntax like import `item.subitem.subsubitem`, each item except for the last must be a package; the last item can be a module or a package but **can’t be a class or function or variable defined in the previous item**.

```Python
# using requests package
import requests

resp = requests.get("https://httpstat.us/200")

print(resp.status_code)
for header in resp.headers:
    print(f"{header}: {resp.headers[header]}")
```

### Importing packages and modules using `from .. import` statement

* `from <package | module> import <subpackage | module | object>` - From a package or a module we can import a subpackage or a module or an object like class or function.

```Python
# from requests package import utils module
from requests import utils
utils.urlparse("https://httpstat.us/200")

# from requests package, utils module import urlparse function
from requests.utils import urlparse
urlparse("https://httpstat.us/200")
```

### Importing packages using wildcard `*`

* Not a recommended approach.

> The `import` statement uses the following convention: if a package’s `__init__.py` code defines a **list** named `__all__`, it is taken to be the list of module names that should be imported when from package `import *` is encountered

```Python
# The below changes need to be made in the __init__.py of the package for importing all modules or importing everything inside a module.

# __init__.py
# import the below modules when the package gets imported
import module1, module2

# Importing with the wildcard form
__all__ = ["module1"]

# above changes can be tested with
# import package
# dir(package)
```

## Absolute vs Relative Imports in Python

### `PYTHONPATH` environment variable

> * When you start a Python interpreter, one of the things it creates automatically is a list that contains all of directories it will use to search for modules when importing. This list is available in a variable named sys.path.
> * `PYTHONPATH` is related to sys.path very closely. `PYTHONPATH` is an environment variable that you set before running the Python interpreter. `PYTHONPATH`, if it exists, should contain directories that should be searched for modules when using import. If `PYTHONPATH` is set, Python will include the directories in sys.path for searching.
> * When you call import in the Python interpreter searches through a set of directories for the name provided. The list of directories that it searches is stored in sys.path and can be modified during run-time. To modify the paths before starting Python, you can modify the `PYTHONPATH` environment variable.
> * Empty `''` entry in `sys.path` means the current directory.
>
> -[`sys.path` and `PYTHONPATH`](https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial)

### Absolute Imports

* When the project's root folder is available in `sys.path`, absolute import contains the absolute path to the module starting from the root package inside the project's directory.

* Absolute import usage is recommended.

```Python
# ProjectRoot/
#   simple_package/
#       simple_module.py
#       __init__.py
#   package2/
#       module1.py
#       __init__.py
#   app.py

# Below imports are present in app.py
# PYTHONPATH contains ProjectRoot

# Arrange the imports alphabetically

# import module1 from package2
from package2 import module1
# package simple_package will be found in PYTHONPATH
from simple_package.module1 import SimpleClass

simple_class = SimpleClass()
module1.utility_method()
```

### Relative Imports

* Uses package or module location relative to the python file containing the import statement

```Python
# ProjectRoot/
#   simple_package/
#       simple_module.py
#       __init__.py
#   package2/
#       module1.py
#       __init__.py
#   app.py

# If module1 requires simple_module, then it can be imported using relative imports
from ..simple_package import simple_module

# To import simple_module in __init__ of simple_package using relative imports
from . import simple_module

```

* If absolute import is too long, relative imports can be used.

---

## References

* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)

* [Python3 modules](https://docs.python.org/3/tutorial/modules.html)

* [Absolute vs Relative Imports in Python](https://realpython.com/absolute-vs-relative-python-imports/)

# Python scope and LEGB rule

* LEGB - Local, Enclosing, Global and Builtin

* local scope - names defined inside function
* global scope - module level scope (outside all the functions)

* Scope decides the names visible to a piece of code.

* Python scopes are implemented as dictionaries. They are stored in special attribute `__dict__` in objects. This dictionary is creates a **namespace**.

* Names are looked up through different levels of scope.

* We get `NameError` when the name in not found in any of the scope.

## Module namespace

```Python
import sys

# Returns all the names in the module namespace.
print(sys.__dict__.keys())
```

* Names in a module namespace(applies to any namespace) can be accessed through either of the two syntax
  * **dot notation** - `module_name.name`
  * **Through `__dict__`** - `module_name.__dict__['name']`

## Scope resolution of a name using LEGB rule

### Local scope

* Also refered to as function scope.
* created on every function call. Contains the local variables defined within functions or lambda expressions.
* This includes nested functions as well. A new instance of nested function is created on invoking the enclosing outer function everytime.

## Enclosing scope

* Applies to closures(nested functions)
* Nested functions can access names defined within the enclosing/outer function.
* Names in this scope are referred to as **nonlocal names**.

## Global/Module scope

* Outside of all classes and functions inside a python module.

## Builtin scope

* During runtime, names(exception, collections like list, dict etc, keywords, functions) from python becomes available to our program.

* To lookup the names from the builtins module `dir(__builtins__)`

* Though not mandatory, we can also import builtins module `import builtins`

**NOTE**: To modify a global variable within a function, we need to declare the variable with **global** keyword. Similarly to modify a variable in the enclosing scope, the nested function should define the variable with **nonlocal** keyword. To access their values, these keywords are not required, these declarations are required when we are about to modify the variable values.

## `global` keyword

* The statement consists of the **global** keyword followed by one or more names separated by commas.

* Can be used to define a variable in global scope, or update the value of an existing global variable.

## `nonlocal` keyword

* If you want to modify nonlocal names in enclosing scopes of nested functions, then you need to use a **nonlocal statement**.
* **nonlocal statement** cannot create a new variable in the enclosing scope.

## Closure

* Nested function + enclosing scope = closure
* Outer functions that return nested function are referred to as **closure factory**.
* Preserve the values in the enclosing scope and use it at a later point in time.

* `functools.partial` - makes use of closures to define new function objects.

## `import` statement

* when using import, then name gets added to the current module's global scope /local scope depending on where the import statement is used.

**NOTE** - Names inside classes, exceptions and list comprehensions donot fit in to the LEGB rule.

## Classes and instances

* Accessing an attribute using the dot notation on the instance does the following:
  * Check the instance local scope or namespace first.
  * If the attribute is not found there, then check the class local scope or namespace.
  * If the name doesn’t exist in the class namespace either, then you’ll get an `AttributeError`.

> In general, good OOP practices recommend not to shadow class attributes with instance attributes that have different responsibilities or perform different actions. Doing so can lead to subtle and hard-to-find bugs.

* `class_name.__dict__` lists the class attributes while `instance.__dict__` lists the instance attributes.

## Scope related builtin functions

* Never uses any of these methods to update the value of the variables in any scope.
* Think of the results returned by `globals()` and `locals()` as **deep copy** of the names in the current global/local namespace. These functions should only be used for **readonly** operations.

  * `globals()` - returns names in current global scope
  * `locals()` - names in the current local scope(ex: inside a function). When used in global scope it is same as `globals()`
  * `dir()` - without argument, this method lists the names in the current scope. If an object is passed to this method, it lists the attributes on that object. Used for debugging purposes and interactive use.
  * `vars()` - returns the `__dict__` attribute of the object or module or instance. `vars(sys) is sys.__dict__`. Without arguments `vars()` is same as `locals()` in local scope and same as `globals` in global scope. If you call `vars()` with an object that doesn’t have a .__dict__, then you’ll get a `TypeError`.__name__

---

## References

* [Python Scope & the LEGB Rule: Resolving Names in Your Code](https://realpython.com/python-scope-legb-rule/)

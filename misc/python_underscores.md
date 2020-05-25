# Underscore naming convention in Python

* Single Leading Underscore: `_var`
* Single Trailing Underscore: `var_`
* Double Leading Underscore: `__var`
* Double Leading and Trailing Underscore: `__var__`
* Single Underscore: `_`

## Single Leading Underscore: `_var`

> Single underscores are a Python naming convention indicating a name is meant for internal use. It is generally not enforced by the Python interpreter and meant as a hint to the programmer only.

* By convention, underscore prefixed variables and methods should not be considered as part of the public interface.
* Not enforced by python interpreter.
* While importing modules using **wildcard import `*`**, single underscore prefixed variables and methods are not imported.
* PEP8 recommendation is to **avoid using wildcard imports**.

## Single leading underscore in class members

* Members with single underscore prefix serve as protected members in inheritance scenarios.

```Python
class SExample:
    _shared_state = {}
    def __init__(self):
        # self will lookup the method _protect on the
        # class of the instance(self) first and then if its not
        # found it will move up the hierarchy.
        self._protect()
        # This will also refer to the dictionary of the subclass
        # Since self is an instance of the DExample.
        print(self._shared_state)

    def _protect(self):
        print("From SExample protect")

class DExample(SExample):
    _shared_state = {"state": "Running"}
    def __init__(self):
        super().__init__()
    def _protect(self):
        print("From DExample protect")

# prints From DExample protect
d = DExample()
```

## Single Trailing Underscore: `var_`

* A single trailing underscore is used by convention to avoid naming conflicts with Python keywords.

```Python
def get_class_name(class_):
    return class.__name__
```

## Double Leading Underscore: `__var`

* Name mangling affects all names(class attributes as well as methods) that start with two underscore characters (“dunders”) in a class context.

* Names prefixed with double underscores inside a class is name mangled to avoid being overridden in subclasses.

* It also prevents the member usage/invocation from outside the class (making the members private to that class).

* Name mangling is transparent to the developer.

```Python
class Parent:
    def __init__(self, arg):
        self.__arg = arg

class Child(Parent):
    def __init__(self, arg):
        super().__init__(arg.upper())
        self.__arg = arg

dir(Parent('hello'))

child = Child('Hello')
dir(child)
# direct usage is not allowed
print(child.__arg)

print(child._Parent__arg)
print(child._Child__arg)
```

* In inheritance scenarios, attributes with dunder prefixes can help define class exclusive members thereby avoiding conflicts.

* Note from the below example, name of the class where the self statement is executed is used for unmangling, even though self can be an instance of the subclass.

```Python
class SExample:
    __shared_state = {}
    def __init__(self):
        # here name unmangling will resolve the below call to
        # _SExample__protect because self is present in the SExample class.
        self.__protect()
        # here name unmangling will resolve the below call to
        # _SExample__shared_state
        print(self.__shared_state)

    def __protect(self):
        print("From SExample protect")

class DExample(SExample):
    __shared_state = {"state": "Running"}
    def __init__(self):
        super().__init__()
        # here name unmangling will resolve the below call to
        # _DExample__protect
        self.__protect()
        # here name unmangling will resolve the below call to
        # _DExample__shared_state
        print(self.__shared_state)

    def __protect(self):
        print("From DExample protect")
```

## Double Leading and Trailing Underscore: `__var__`

* Name mangling is not applied if a name starts and ends with double underscores.

* Such names are reserved for special usage in the language.

> It’s best to stay away from using names that start and end with double underscores (“dunders”) in your own programs to avoid collisions with future changes to the Python language.

## Single Underscore: `_`

* Used to indicate that a variable is **temporary or insignificant**

* This interpretation is **convention** only and there’s no special behavior triggered in the Python interpreter.

```Python
# loop variables
for _ in range(10):
    print('Hello World')

# unpacking tuples and leave insignificant ones
def csv_content():
    return ('Name', 'Email', 'Age', 'Gender')

name, _, _, gender = csv_content()
print(name)
print(gender)
```

---

## References

* [The Meaning of Underscores in Python](https://dbader.org/blog/meaning-of-underscores-in-python)

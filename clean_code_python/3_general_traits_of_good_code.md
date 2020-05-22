# General traits of Good code

## Design by contract

* Contract between client code and the called code.
* API code can have the preconditions, postconditions, invariants and side effects documented in its doc strings.
* precondition - validation of parameters passed from the client
* postcondition - value returned by the API code.
* invariants - things that are constant during the code execution
* If the precondition fails, issue is with the client code(calling code) and if the postcondition fails issue is with the API code(called code)
* In this approach, usually the **API code does the precondition checks**. This is refered to as demanding approach.
* In precondition value of the parameters are checked. **Type checks are not performed**. Type checking is better left to static type checking tools like mypy.
* For gaining confidence on the postcondition, unit tests can be used.

* In this approach, if the preconditions are not met, client will not call the component.

* Python does not have native support for design by contract. But we have third party libraries that can support this.

* We can have `assert` statements to check preconditions and disable them in production by running the python interpreter with **-O** flag.

## Defensive programming

* Handling error scenarios that are expected as well as dealing with errors that should never occur.

* Error handling approaches
  * Value substitution
  * Error logging
  * Exception handling

### Value substitution

* Providing a sensible default for missing parameters.
* Returning a sensible default when the result cannot be computed due to missing parameters. Should be cautious in selecting this approach.

```Python
db_connection = {"dbport": 5432}

# Here the default value is returned when the key 'dbhost'
# is not found in the dictionary
print(db_connection.get("dbhost", "localhost"))
```

* Robustness vs correctness issue. Sometimes this way of handling can mask errors.

### Exception handling

* A function should not be raising too many exceptions.
* An exception should be raised only to notify erroneous situation to the caller.

* Handling exceptions at right level of abstraction
* Do not expose tracebacks, since they contain stack trace which could reveal the internals of an intellectual property. This could cause security issues.
* Avoid empty except blocks.
* Include original exception when raising a different exception from an except block. `raise new_ex from causing_ex` is the syntax in python 3. Original exception can be accessed from the `__cause__` attribute on the new exception.

* Assertions should not be mixed with business logic or used as control flow mechanism. Should be used for catching defects. Program should be stopped on `AssertionError`. Always assert on a computed value like a variable rather than on a dynamic expression like function call. This would make it easy to reproduce the situation that caused the assert to fail.

## Separation of concerns

* Components should be dealing with single responsibility.
* **Cohesion** means that objects should have a small and well-defined
purpose. Cohesive components are highly reusable.
* Coupling - two or more objects depend on each other. This is not desired.
* Target **high cohesion and low coupling** while designing

## DRY(Dont Repeat Yourself)/OAOO(Once And Only Once)

* Code with same functionality should not be duplicated at multiple places in the same codebase.
* Duplication affects maintainability

## YAGNI(You Aint Gonna Need It)

* Don't design anticipating future requirements. It can lead to over engineering.
* Always write software addressing current requirements but still making it easier to accomodate new requirements.

## KIS (Keep It Simple)

* Design the solution simple enough to solve the problem in hand correctly.
* Simpler solutions are more maintainable.

> Remember the zen of Python: simple is better than complex.

## EAFP(Easier to Ask Forgiveness than Permission)/ LBYL(Look Before You Leap)

> EAFP - This means try running some code, expecting it to work, but catching an exception if it doesn't, and then handling the corrective code on the except block

* LBYL is opposite of EAFP. Python encourages EAFP(From zen of python **explicit is better than implicit**).

## Inheritance (specialization)

* Inheritance leads to coupling between base and derived classes

* Inheritance **should not be used for code reuse**. For code reuse, composition is preferred as it leads to a cohesive solution.

* Inheritance can be used to define interfaces in the form of abstract base classes that can be overridden by the derived classes.

* Inheritance is useful in defining the **exception hierarchy**.

### Anti-patterns for inheritance

* We should not extend from a base classes because of few functionalities. For instance, extending from `dict` just because we need to access by subscript is incorrect. With this we also add other unnecessary functionalities from `dict` to the derived class.

## Multiple inheritance

* With multiple inheritance, we can implement mixins
* Method resolution order - resolves calls to base class methods

```Python
# Printing the method resolution order for a class called ConcreteClass
print([cls.__name__ for cls in ConcreteClass.mro()])
```

* Method resolution order is explained very well in this [article](http://www.srikanthtechnologies.com/blog/python/mro.aspx). The same article is stored in my [pocket library](https://app.getpocket.com/read/2723074421)

> You also get the assurance that, in `__mro__`, no class is duplicated, and no class comes after its ancestors, save that classes that first enter at the same level of multiple inheritance are in the `__mro__` left to right.
> Every attribute you get on a class's instance, not just methods, is conceptually looked up along the `__mro__`, so, if more than one class among the ancestors defines that name, this tells you where the attribute will be found -- in the first class in the `__mro__` that defines that name.
> `mro` can be customized by a metaclass, is called once at class initialization, and the result is stored in `__mro__`
>
> [SO: What does “mro()” do?](https://stackoverflow.com/questions/2010692/what-does-mro-do)

## Mixins

* Solving problem using single inheritance

```Python
class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token
    def __iter__(self):
        yield from self.str_token.split("-")

class UpperCaseTokenizer(BaseTokenizer):
    def __iter__(self):
        return map(str.upper, super().__iter__())

# Here the tokenizer was changed to inherit from UpperCaseTokenizer
# instead of the BaseTokenizer
class Tokenizer(UpperCaseTokenizer):
    pass
```

> A mixin is a base class that encapsulates some common behavior with the goal of reusing code. Typically, a mixin class is not useful on its own, and extending this class alone will certainly not work, because most of the time it depends on methods and properties that are defined in other classes.

* Above solution can also be written using mixins exploiting the MRO.

```Python
class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token
    def __iter__(self):
        yield from self.str_token.split("-")

class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())

class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass

# prints the method resolution order
print(Tokenizer.mro())
```

## Arguments in functions and methods

* Keyword and positional parameters
* Parameters are always passed by value in Python.
* Avoid mutating function parameters.
* Refactor functions with large number of parameters. For a caller to know how to provide all the parameters of that function, makes the abstraction a weaker one and increases the coupling between the functions.

### Variable number of arguments

* `*args` - to accept variable number of positional parameters.

```Python
# unpacking
first, *rest = [1, 2, 3, 4, 5]
print(first)
print(rest)

def simple_func(x, y):
    print(x, y)

point = (1, 2)
simple_func(*point)

# packing multiple parameters in to one
def test_func(*args):
    print(type(args)) # tuple
    print(args)

test_func("Hello", "World")
```

* Unpacking is often used iteration

```Python
l1 = list(range(1, 10))
l2 = list(range(11, 20))

# Unpacking to iterate through all the elements of both the lists
print(max(*l1, *l2))

# We can also implement the same using the itertools.chain
import itertools
print(max(itertools.chain(l1, l2)))
```

* `**kwargs` - packing and unpacking of keyword arguments

```Python
def simple_func(first, second):
    print(first, second)

# using keyword arguments
simple_func(first="Foo", second="Bar")

param_dict = {"first": "Hello", "second": "World"}
# unpacking
simple_func(**param_dict)

def test_func(**kwrgs):
    print(type(kwargs))
    print(kwargs)

# pack the arguments in to a dictionary
test_func(first="Hello", second="World")
```

* Keep the number of arguments to be as minimal as possible. Related parameters can be grouped in to a single object(known as **reification**). If we cannot reify, then We can use the variable args.

> When functions have a more general interface and are able to work with higher-level abstractions, they become more reusable
> Work with immutable objects, and avoid side-effects as much as possible.

## Orthogonality in software

* Orthogonality - making the modules independent of each other. High cohesion. Easy to make changes without regressing other components/modules.

## Structuring the code

* In python a large module can be split in to a package containing many smaller modules, **without breaking any import statements**

* All the things that were previously present in the large module can be added to the new package's `__init__.py` file, so the older import statements are still valid.

---

## References

* [Clean code in python by Mariano Anaya](https://www.oreilly.com/library/view/clean-code-in/9781788835831/)

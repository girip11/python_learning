# Python decorators

> Python’s functions are first-class objects. You can assign them to variables, store them in data structures, pass them as arguments to other functions, and even return them as values from other functions. - [Python’s Functions Are First-Class](https://dbader.org/blog/python-first-class-functions)

## Python functions

* Python assigns an **internal name** to every function during its creation. This internal name can be accessed via the `__name__` attribute on the function object

```Python
def say_hello(name):
    print(f"Hello, {name}")

greet = say_hello

print(greet.__name__)
print(say_hello.__name__)

# deletes only the reference to the function object
# and not the function object itself
del say_hello

# still the function is invoked
greet('John')
```

* Higher order functions - functions that accept functions as parameters

* Function definition can be nested inside another function. Such nested functions can be returned as the output from the function containing it. With this, we can create **closures**.

> A closure remembers the values from its enclosing lexical scope even when the program flow is no longer in that scope. [Python’s Functions Are First-Class](https://dbader.org/blog/python-first-class-functions)

## Objects behaving as functions

* Objects that implement the special method `__call__` are callable (i.e) these objects can be called like a function with arguments passed to the object.

* Objects with this `__call__` method are said to have implemented the **callable interface** and return `True` when passed to the builtin function `callable()`.

```Python
class StringTransformer:
    def __init__(self, op):
        self.op = op

    def __call__(self, input_str):
        tranform_method = getattr(input_str, self.op)
        return tranform_method()

capitalize = StringTransformer("capitalize")

# object called like a function
# executes the call method on that object
capitalize("hello world")

# to test if an object is callable or not
# we can use the builtin function `callable`
print(callable(capitalize))

# Prints False
print(callable("strings are not callable objects"))
```

## Decorators

* Decorators usually wrap a function and extend/modify its behavior

```Python
def greeting_decorator(func):
    # Note the inner function takes similar parameters to that of
    # the greet_person
    def decorate_greeting(name):
        print("*******************")
        func(name)
        print("*******************")

    return decorate_greeting

def greet_person(name):
    print(f"Hello, {name}")

greet_person = greeting_decorator(greet_person)
greet_person('John')
```

## Decorators using the **pie syntax** (@)

* `@<decorator_name>` (more generally `@<expression>`) before the function definition. Note that the decorator name is specified and no paranthesis is used following the decorator name.

* `greeting_decorator` is invoked and executed by the interpreter for every **@annotation** and the return value of this function is assigned to the names of the functions that its decorating.

```Python
# Note the func argument is automatically passed to this greeting_decorator
def greeting_decorator(func):
    print(f"{greeting_decorator} is executed for every @annotation")

    # Notice that the actual decorating function
    # should accept the same arguments as the function being decorated
    # OR
    # the actual decorating function can accept
    # generic arguments (*args, **kwargs)
    def decorate_greeting(name):
        print("*******************")
        func(name)
        print("*******************")

    return decorate_greeting

@greeting_decorator
def greet_person(name):
    print(f"Hello, {name}")

# prints decorate_greeting
print(greet_person.__name__)

@greeting_decorator
def greet_world():
    print(f"Hello, world")

print(greet_world.__name__)

greet_person('John')
```

* `@functools.wrap` is used to preserve the information of the function which is about to be decorated.

```Python
import functools

def greeting_decorator(func):
    @functools.wraps(func)
    def decorate_greeting(name):
        print("*******************")
        func(name)
        print("*******************")

    return decorate_greeting

@greeting_decorator
def greet_person(name):
    print(f"Hello, {name}")

print(greet_person.__name__)
```

## Decorator functions with arguments

* The function to be decorated is always passed as argument to the function pointed by the **@annotation expression (notice the term expression)**.

* The **@annotated expression** should always return a **callable object** (function or an object that can behave like a function aka **callable object**) that can accept a function as the parameter.

* This is important to know because, in cases where the decorator method following **@** has to be passed arguments.

```Python
import functools

def with_offset(x_offset = 0, y_offset = 0):

    def inner_func(func):

        # Notice the decorator inside the inner function
        @functools.wraps(func)
        def decorator_func(point):
            new_point = func(point)
            return Point(new_point.x + x_offset, new_point.y + y_offset)

        return decorator_func

    return inner_func

# Notice the function with_offset is invoked with arguments other than func.
# But decorating function should accept func as its only argument
# So in this case with_offset
@with_offset(1, 1)
def compute_new_position(point):
    # implementation
```

## Decorators with generic arguments

* A function can have many decorators. So its good practice to write decorating functions with generic arguments, since those decorators can be passed another decorating function.

```Python
import functools

def greeting_decorator(func):
    @functools.wraps(func)
    def decorate_greeting(*args, **kwargs):
        print("*******************")
        func(*args, **kwargs)
        print("*******************")

    return decorate_greeting

@greeting_decorator
def greet_person(name):
    print(f"Hello, {name}")

greet_person('John')

@greeting_decorator
def greet_world():
    print(f"Hello, world")

greet_world()
# to print the name of the decorator behind greet_world
# prints decorate_greeting
print(greet_world.__name__)
```

## Multiple decorators on the same function

* While parsing the pie syntax, the decorators **are parsed bottom up**.  This leads to the **decorator evaluation order** `auth(timer(deliver_msg))`.

* While execution, interpret the **execution order** as **`auth decorator` calls `timer_decorator` which inturn calls the `deliver_msg` function**

```Python
import functools

def timer(func):
    @functools.wraps(func)
    def timer_decorator(*args, **kwargs):
        print("Inside timer decorator")
        func(*args, **kwargs)
    return timer_decorator

def auth(func):
    @functools.wraps(func)
    def auth_decorator(*args, **kwargs):
        print("Inside auth decorator")
        func(*args, **kwargs)
    return auth_decorator

# Equivalent to auth(timer(deliver_msg("Hello")))
# While parsing decorators are processed bottom up
# First to the timer decorator, deliver_msg is passed
# To the auth decorator, the result of the timer decorator is passed
# Only when auth succeeds timer will be called and the deliver_msg execution
# alone is timed.
@auth
@timer
def deliver_msg(msg):
    print(f"Message: {msg}")
```

* Example for **decorators that accept optional arguments** can be found from a [snippet from python cookbook](https://github.com/dabeaz/python-cookbook/blob/master/src/9/defining_a_decorator_that_takes_an_optional_argument/example.py)

```Python
def decorator(func = None, *, kwarg1 = [default_value]...):
    pass
```

## [Decorators on classes](https://realpython.com/primer-on-python-decorators/#decorating-classes)

* Applies on the class.
* `dataclass` decorator in the `dataclasses` module

> A common use of class decorators is to be a simpler alternative to some use-cases of metaclasses.

## Stateful decorators

State can be stored using

* Using the wrapper function attributes
* Using class as a decorator instead of a function.

### Stateful decorators using function attributes

```Python
import functools

def count(func):
    @functools.wraps(func)
    def wrapper_count(*args, **kwargs):
        wrapper_count.count += 1
        return func(*args, **kwargs)
    # Using dynamic attributes on a function object
    wrapper_count.count = 0
    return wrapper_count

@count
def say_hello(name):
    print(f"Hello, {name}")

say_hello("John")
say_hello("Jane")
print(vars(say_hello))
print(say_hello.count)
```

### Stateful decorators using classes

* Class should have `__init__` method that can accept a `func` (or aclass if applied on class) as its argument

* Objects of the decorator class should be **callable** (i.e)  implement the `__call__` method. **This method acts as the nested wrapper method when functions are used as decorators.**

* Class as a decorator can be used for storing the state.

```Python
import functools

class count:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)

@count
def say_hello(name):
    print(f"Hello, {name}")

say_hello("John")
say_hello("Jane")
print(vars(say_hello))
print(say_hello.count)
```

* If the decorator has to accept arguments, then `__init__` method accepts those arguments and the `__call__` function accepts the function/class to be decorated.

```Python
import functools
import time

# Here the example is not important. what needs to be observed here
# is how the init and call methods are written
class RateLimit:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper_rate_limit(*args, **kwargs):
            if self.count < self.limit:
                self.count += 1
                return func(*args, **kwargs)
            else:
                print("Rate limit reached. Introducing wait time")
                time.sleep(1)
                self.count = 0

        return wrapper_rate_limit

@RateLimit(3)
def print_msg(msg):
    print(f"{msg}")

for _ in range(10):
    print_msg("Hello")
```

---

## References

* [Python decorators](https://realpython.com/primer-on-python-decorators/)
* [Python decorators](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/PythonDecorators.html)

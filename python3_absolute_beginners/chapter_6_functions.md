# Chapter-6: Functions

Functions follow **snake_case** as the naming convention. Function names are usually verbs while the variable names tend to be nouns.

## Function syntax

```Python
# function syntax
# ================
# def function_name(param1, param2..):
#   """
#   This is a doc string. This can be #   used to describe about the
#   function. doc string should be
#   the first thing in a function.
#   """
#   function_body
#   return None # you could choose to return a value. default return value is None

def print_hello_world():
  """
    prints message "Hello world" to the console
  """
  print("Hello world")

def print_message(msg):
  print(msg)

def get_string_length(input_string):
  """
  returns the length of input_string
  """
  return len(input_string) if (isinstance(input, str) and input_string) else 0

# function call
print_hello_world()
print_message("Hello world")
# below arguments are referred to as positional arguments
print(get_string_length("Palindrome"))
```

## Default parameters and keyword arguments

```Python
# function with default parameters
import random
def get_random_number(min= 0 , max = 100):
  """
    returns random number from min to max
  """
  return random.randint(min, max)

# function call with default parameters
random_number = get_random_number()

# calling a method with keyword arguments. note that the order of arguments doesnt matter in this case
random_number = get_random_number( max = 1000, min = 10)
```

* Default values can be assigned to parameters from function calls.

```Python
def default_val():
    print("default_val method called")
    return [0]

# l is assigned the output of the function default_val
# The function is not called everytime to assign default value
# the function is called only once, and the return value is used everytime
# this parameter is missed in the function call
def example(n, l = default_val()):
    print(f"List ID: {id(l)}")
    print(l)

example(1)
example(2)
```

* Objects can also be assigned to parameters.

```Python
# l is assigned a list. Everytime the parameter is missed
# out in the function call, same object is used.
def example(n, l = list()):
    l.append(n)
    # New list is not created on every function call
    # This can be verified by looking at the id of the default parameter value
    print(f"List ID: {id(l)}")
    print(l)

example(1)
example(2)

example(3, [])

example(4)
example(5)
```

## Disabling keyword argument and enabling only positional argument

* From python 3.8 onwards, we can force positional only arguments using `/` marker. All paramerets to the **left** of the `/` marker are positional parameters only.

```Python
def greet(name, /, msg="Hey"):
    print(f"{msg}, {name}")

# Raises TypeError: greet() got some positional-only arguments
# passed as keyword arguments: 'name'
greet(name="John", msg = "Hello")

# Works
greet("John", msg="Hello")
greet("John", "Hi")
```

## Passing variable arguments to the function

> If the form `*identifier` is present, it is initialized to a **tuple** receiving any excess positional parameters, defaulting to the **empty tuple**. If the form `**identifier` is present, it is initialized to a **new ordered mapping(`dict`) receiving any excess keyword arguments, defaulting to a new empty mapping of the same type**. Parameters after `*` or `*identifier` are **keyword-only parameters** and may only be passed used keyword arguments. - [Function Definitions in python](https://docs.python.org/3/reference/compound_stmts.html#function-definitions)

* Using `*args` and `**kwargs` to capture variable number of arguments

**NOTE**: In a function call, positional arguments comes before keyword arguments. In a function definition, the convention is to place mandatory parameters followed by **parameters with default values**, `*args` and then `**kwargs`.

`*` and `**` can be used in function calls too for unpacking lists and dictionaries. First these parameters are expanded as `tuple` and `dict` respectively and then passed to the function.

```Python
# convention is to call the * parameter as args
def print_values(*args):
    # args is a tuple here. verify using type(args)
    print(args)

print_values("Apple", "Mango", "Orange", 1, 10.5)

# using splat to pass entry list entry as a parameter
print_values(*["Apple", "Mango", "Orange"])

# convention is to call the ** parameter as kwargs
def print_key_value_pairs(**kwargs):
    # kwargs is a dict.
    for key in kwargs:
        print("Key: {0!s}, value: {1!s}".format(key, kwargs[key]))

print_key_value_pairs(one = 1, two = 2, three = 3)

# splat dict
print_key_value_pairs(**{"one": 1, "two": 2, "three": 3 })
```

* Using `*` to enforce keyword only arguments following `*`. Available from **Python 3 onwards**

```Python
# atleast 1 Keyword argument should follow *
def simple_func(pos_arg, def_arg = None, *, kwarg1 = '',**kwargs):
    print(f"pos_arg: {pos_arg}")
    print(f"def_arg: {def_arg}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

simple_func(10, name="John Doe", age = "25")

# kwarg1 should be explicitly specified to assign a value
simple_func(pos_arg = 10, kwarg1 = "Hello", name="John Doe", age = "25")

simple_func(10, def_arg = "default arg" , kwarg1 = "Hello", name="John Doe", age = "25")
```

## Docstring convention

* First line - short description of the function
* Function parameters description
* Longer description of the function explaining algorithm used if any
* Return value description
* Example function call with optional arguments, keyword arguments.
* Information on side-effects, exceptions

Read about [PEP 257: Docstring conventions](https://www.python.org/dev/peps/pep-0257/)

```Python
def my_function(param):
    """
    Summary line.

    Extended description of function.

    Parameters:
    arg1 (int): Description of arg1

    Returns:
    int: Description of return value

    """

    return None

print(my_function.__doc__)
```

## Global statement

If a function uses global variables, then we use **global** statement to declare the usage of those global variables.

Using **global** statement new global variables can be defined from inside a function.

```Python
planet1 = "mercury"
planet2 = "venus"
planet3 = "earth"

def capitalize():
  global planet1, planet2, planet3
  planet1 = planet1.upper()
  planet2 = planet2.upper()
  planet3 = planet3.upper()
  planets = ",".join([planet1, planet2, planet3])
  print(planets)
  print(vars())
```

## Variable Scopes

* Symbol table to track names used in the program. `vars()` built-in can help dump the values as dictionary.
* Variables created in main program's symbol table known as **global variables**. `globals()` builtin to view them.
* Variables created inside function stored in symbol table specific to that function.`locals()` builtin to view them.

* All functions can access global variables. if local variables have same name as global variables, then the global variables cannot be used inside the function, known as **shadowed globals**

* If not explicitly specified as `global`, variables defined inside functions act as local variables. Global and local variables

```Python
def simple_function1():
    greeting = "Hi"
    print(f"Greeting from simple_function1:{greeting}")

greeting = "Hello"
print(f"Initial Greeting: {greeting}")
simple_function1()

def simple_function2():
    global greeting
    # declare that we are referring to greeting global variable
    greeting = "Hey"
    print(f"Greeting from simple_function2:{greeting}")

simple_function2()
print(f"Final greeting :{greeting}")
```

## `globals() vs locals() vs vars()`

* `locals()` - returns a dictionary of names declared in **current namespace**. If used inside a function namespace, returns dictionary with local variables defined at that point. Changes made to this dictionary does not reflect back to the namespace.  
* `globals()` - returns a dictionary of names declared in **module namespace**.
* `vars([obj])` - returns dictionary of current namespace or its argument. Without argument it is equivalent to `locals()`. If passed an argument, `vars()` returns the `__dict__` attribute of the input object. Changes made to this dictionary are reflected in the namespace. Use `vars()` to get the object `__dict__`

* `dir([obj])` - returns list of symbols(attributes and method) in current namespace or of passed object. `dir()` is same as `locals().keys()`

```Python
def simple_function1():
    greeting = "Hi"
    print(f"Greeting from simple_function1:{greeting}")
    print(locals())
    print(globals())

simple_function1()

def simple_function2():
    global greeting
    greeting = "Hey"
    print(f"Greeting from simple_function2:{greeting}")
    print(locals())
    print(globals())

simple_function2()

class SimpleClass:
    class_attr = "hello"
    def __init__(self, arg):
        self._inst_attr = arg

vars(SimpleClass)
print(SimpleClass.__dict__)
vars(SimpleClass('Hello'))
print(SimpleClass('Hello').__dict__)
```

## Passing lists and dictionaries to functions

* Integers, floats are passed by value to functions.
* String, tuple are immutable themselves. so when passed to function as arguments, those values remain unchanged.
* In case of mutable structures like lists, set and dictionaries, only the reference is passed. It is possible to modify these sequences from inside the function and cause side effects.

## Nesting of functions

* In python, a function can contain other function definitions within it.
* The nested/inner functions **are not defined until the parent** function is called. Equivalent to local variable being alive only in the function scope.

```Python
def get_url(protocol, host, port):

    # A new instance of this inner function is created every time,
    # the get_url function is invoked
    def format_url():
        return f"{protocol}://{host}:{port}"

    # New id is printed everytime this function is called
    print(id(format_url))
    return format_url()
```

* [Non local variables](https://www.python-course.eu/python3_global_vs_local_variables.php) - variables defined in the outer function scope are non local variables to the nested function.

```Python
def search_record(record_type, email):

    # Note the nested functions can access the variables of the outer
    # function
    def get_record():
        print(locals())
        # In this case the record_type and email are non local variables.
        return {"record": record_type, "email": email}

    return db.search(get_record())

search_record('Student', 'john@example.com')
```

* Those functions are visible and invokable only from within the outer function unless the function returns the inner function as its return value.

```Python
def get_record_template_creator(record_type):

    # This method can be thought of a closure since the
    # state(value of the record_type) is fixed in the returned function
    def create_record_template(name, email):
        return {
            'record':  record_type,
            'name': name,
            'email': email
        }

    # return the function that can create template
    # for a particular record type
    return create_record_template

create_student_template = get_record_template_creator('Student')
create_student_template('John', 'john@example.com')

create_teacher_template = get_record_template_creator('Teacher')
create_teacher_template('Jane Doe', 'jane@example.com')
```

## Python closures

> * A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
> * A closure—unlike a plain function—allows the function to access those captured variables through the closure’s copies of their values or references, even when the function is invoked outside their scope.
> [-Python closures GFG](https://www.geeksforgeeks.org/python-closures/)

```Python
def get_url_creator(protocol):

    # this function is an example of closure
    # since the value of parameter protocol is carried on to
    # this method's scope
    # This nested function is called as **inner function**
    def create_url(host, port):
        return f"{protocol}://{host}:{port}"

    return create_url

url_creator = get_url_creator("http")

# Notice the value of the outer function parameter *protocol*
# is remembered by the returned function, even though the get_url_creator
# is completed and out of scope
print(url_creator("example.com", 8080))
print(url_creator("mydomain.com", 8000))
```

**NOTE**: **Closures are late binding in python**. This means the value of the variable in the enclosed scope is looked up and substituted only when the closure is called. This behavior is same for lambdas as well as functions

```Python
# In the enclosed scope of the lambda, the value of i is stored as 10
# which is the for loop end condition
multipliers = [lambda x: (i + 1) * x for i in range(10)]

    # This will print 20 for 10 times
# because when the closure is called the value of i is 10
for m in multipliers:
    print(m(2))

# Fixing the value of the variable
multipliers = [lambda x, i=i: (i + 1) * x for i in range(10)]

for m in multipliers:
    print(m(2))
```

---

## References

* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)
* [Global, Local and nonlocal Variables](https://www.python-course.eu/python3_global_vs_local_variables.php)
* [globals vs locals vs dir](https://stackoverflow.com/questions/32003472/difference-between-locals-and-globals-and-dir-in-python)
* [Force positional arguments only](https://deepsource.io/blog/python-positional-only-arguments/)

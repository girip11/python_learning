# Using decorators to improve our code

* Decorators in python not to be confused with decorator design pattern.

* Decorators can be applied to functions, methods, generators and classes.

## Passing arguments to the decorators

* Decorator function that accepts parameter will have nested function as the actual decorator causing the functions to go one level deeper.

* Classes for decorator. This approach is considered more readable.

### Passing parameters to decorator functions

* First level of function accepts the parameters passed to the decorator. This function returns the inner function.
* Inner Function(level 2) is the actual decorator that accepts the function. This function will return its inner function.
* Nested function(level 3) inside the inner function accepts the parameters passed on to the function when called.

```Python
# Decorator structure when accepting parameters
def decorator_accepting_params(arg1=default,...):
    def decorator_func(func):
        def wrapped_func(*args, **kwargs):
            ...
        return wrapped_func
    return decorator_func
```

### Passing parameters to decorator objects

```Python
class DecoratorClass:
    def __init__(self, arg1=default,...):
        ...

    def __call__(self, func):
        def wrapped_func(*args, **kwargs):
            ...
        return wrapped_func
```

## Common usecases to apply decorators

* Transforming parameters
* Tracing code - dump function call arguments, timing function execution
* Validate parameters
* Implement retry operations
* Repetitive logic can be moved to decorators to simplify classes(DRY)

## Common mistakes with decorator

* Failing to preserve properties of the decorated function, class etc.
* `functools.wraps` can be used in decorator functions to preserve the details(name, docstring) of the function being decorated.
* `functools.update_wrapper(self, func)` - when decorator classes are used and the function is passed to the constructor of the decorator object.

## Dealing with side-effects in decorator

* Avoid side effects in the decorator functions.

* In cases where all the decorated functions needs to be registered to a central place, side-effects are desired.

## DRY using decorators

* When the same logic is repeated atleast three times, think of refactoring the logic in to a decorator.
* Wait until the scenario fits the use of a decorator otherwise decorator could introduce additional complexity

## Decorators and Separation of concerns

* For a decorator to be highly cohesive, it should follow single responsibility principle.

---

## References

* [Clean code in python by Mariano Anaya](https://www.oreilly.com/library/view/clean-code-in/9781788835831/)

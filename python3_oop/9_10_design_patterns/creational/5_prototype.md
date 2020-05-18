# Prototype pattern

> Prototypes are useful when object initialization is expensive, and you anticipate few variations on the initialization parameters. In this context, Prototype can avoid expensive "creation from scratch", and support cheap cloning of a pre-initialized prototype.

* Using a prototypical instance, we create other instances instead of creating using `new`

* In scenarios where the object creation is expensive, we can clone a prototype instance and customize few parameters based on our need.

* In python we can use the **copy module**'s `copy` and `deepcopy` methods to shallow and deep clone objects respectively in many cases. So in python implementing cloning functionality becomes easier.

## Implementation

This is just an example implementation case.

* Abstract base class with `clone()` method. This can also maintain a registry of its concrete classes and their prototypical instance.

* All subclasses will implement the `clone` method and also will register their prototype instance.

* Client calls a factory method on the abstract base class specifying the concrete class whose instance it needs. Then the factory can return a new instance by cloning the appropriate prototype instance from the registry.

![prototype design pattern](./prototype.png)

Example implementation adhering to the above steps can be found [**here**](https://github.com/faif/python-patterns/blob/master/patterns/creational/prototype.py)

## Prototype pattern in python

>The Prototype pattern isn’t necessary in a language powerful enough to support first-class functions and classes. - [Python patterns guide](https://python-patterns.guide/gang-of-four/prototype/)

If the scenario is to populate the object(prototype object) with a set of defaults to the constructor, then to construct the prototype registry we can use any one of the following approaches

* Dictionary of object name to tuple containing class name and parameters that need to be passed to the constructor.
* Dictionary of object name to lambda expression to construct the prototype object
* Dictionary of object name to value created using `functools.partial` that returns a callable with fixed arguments.

---

## References

* [Prototype pattern](https://sourcemaking.com/design_patterns/prototype)
* [Prototype pattern example](https://github.com/faif/python-patterns/blob/master/patterns/creational/prototype.py)
* [Prototype design pattern review in python](https://python-patterns.guide/gang-of-four/prototype/)

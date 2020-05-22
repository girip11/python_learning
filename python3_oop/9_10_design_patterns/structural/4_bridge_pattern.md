# Bridge pattern

* Separate abstraction from its implementation.
* The independent concepts could also be: abstraction/platform, domain/infrastructure, front-end/back-end or interface/implementation.
* Helps to flatten the proliferation of classes whenever a new specialization of the abstraction or a new platform is added. From (m * n) to (m + n)
* Abstraction(interface) hierarchy can grow independently from the platform hierarchy(implementation)

![Bridge pattern](./bridge.png)

**NOTE**: Refer to this well writtern article on [bridge pattern](https://sourcemaking.com/design_patterns/bridge). I have stored a copy in [my pocket library as well](https://app.getpocket.com/read/11409567)

## Implementation notes

* Often interface/abstraction contains a handle to the concrete implementation.
* To instantiate the right concrete implementation, interface/abstraction uses abstract factory.
* Client always interacts with the interface only.

## Sample snippets

* [Bridge pattern example](https://sourcemaking.com/design_patterns/bridge/python/1)
* [Bridge pattern example in python](https://github.com/faif/python-patterns/blob/master/patterns/structural/bridge.py)

---

## References

* [Bridge pattern](https://sourcemaking.com/design_patterns/bridge)
* [Composition over inheritance](https://python-patterns.guide/gang-of-four/composition-over-inheritance/)

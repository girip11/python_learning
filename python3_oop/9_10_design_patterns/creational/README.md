# Creational patterns observations

> Often, designs start out using Factory Method (less complicated, more customizable, subclasses proliferate) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, more complex) as the designer discovers where more flexibility is needed.

* When you need an object to be created, start with factory design pattern (factory pattern could just be a simple factory method).

* When the same object needs multiple stages to get constructed, refactor the factory to builder pattern.

* When the first created object can be used to create other objects (since the instantiation is expensive), then refactor to the prototype pattern

* If we need more dependent objects along with the object (family of objects) for which we wrote the factory, then we might need to refactor to abstract factory.

---

> Sometimes creational patterns are competitors: there are cases when either Prototype or Abstract Factory could be used profitably. At other times they are complementary: Abstract Factory might store a set of Prototypes from which to clone and return product objects, Builder can use one of the other patterns to implement which components get built. Abstract Factory, Builder, and Prototype can use Singleton in their implementation.

---

> Abstract Factory, Builder, and Prototype define a factory object that's responsible for knowing and creating the class of product objects, and make it a parameter of the system. Abstract Factory has the factory object producing objects of several classes. Builder has the factory object building a complex product incrementally using a correspondingly complex protocol. Prototype has the factory object (aka prototype) building a product by copying a prototype object.

---

> Factory Method: creation through inheritance. Prototype: creation through delegation. Prototype doesn't require subclassing, but it does require an "initialize" operation. Factory Method requires subclassing, but doesn't require Initialize.

* Factory method pattern uses inheritance, where subclasses implement the factory method.
* In prototype pattern, we call an object that contains the registry of prototype instances and ask it to create an object of our need from one of the prototypical instances(delegation).

---

> Abstract Factory classes are often implemented with Factory Methods, but they can be implemented using Prototype.

---

## References

* [Design patterns](https://sourcemaking.com/design_patterns)

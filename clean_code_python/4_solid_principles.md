# SOLID Principles

* **S**: Single responsibility principle
* **O**: Open/closed principle
* **L**: Liskov's substitution principle
* **I**: Interface segregation principle
* **D**: Dependency inversion principle

## Single responsibility principle (SRP)

* Software component should be responsible for only one thing. So it should have only one reason to change.

The following checks help us determine whether the class adheres to single responsibility principle.
>
> * What we strive to achieve here is that classes are designed in such away that most of their properties and their attributes are used by its methods, most of the time. When this happens, we know they are related concepts, and therefore it makes sense to group them under the same abstraction.
> * If, when looking at a class, we find methods that are mutually exclusive and do not relate to each other, they are the different responsibilities that have to be broken down into smaller classes.

* Design to the point where the abstraction provided does one thing only. All methods and properties are related to the responsibility of the class.

## Open closed principle (OCP)

* Software component(a class or a module) should be open for extension but closed for modification.

> when something new appears on the domain problem, we only want to add new code, not modify existing code.

* This principle makes effective use of polymorphism. New requirements implement the polymorphic contract.

## Liskov's substitution principle (LCP)

> If S is a subtype of T, then objects of type T may be replaced by objects of type S, without breaking the program.

* This is related to all the subclasses respecting the contract of the base class by implementing the correct behavior. Subclasses should not break the interface(behavior) exposed to the outside code.

* Tools like mypy and pylint can catch if LSP is violated in certain cases like breaking the method signatures in a hierarchy.

> The parent class defines a contract with its clients. Subclasses of this one must respect such a contract. This means that, for example:
>
> * A subclass can never make preconditions stricter than they are defined on the parent class
> * A subclass can never make postconditions weaker than they are defined on the
parent class

* This principle also makes use of polymorphism. Subclasses should honor the polymorphic contract.
* LSP contributes to OCP

## Interface Segregation Principle (ISP)

> ISP states that, when we define an interface that provides multiple methods, it is better to instead break it down into multiple ones, each one containing fewer methods (preferably just one), with a very specific and accurate scope. By separating interfaces into the smallest possible units, to favor code reusability, each class that wants to implement one of these interfaces will most likely be highly cohesive given that it has a quite definite behavior and set of responsibilities.

* Keeping the interface as small as possible makes it highly cohesive.

* Interface segregation principle makes the class implementing the interface adhere to single responsibility principle, since the interface does not contain behaviors that are orthogonal.

## Dependency inversion principle

> The dependency inversion principle (DIP) proposes an interesting design principle by which we protect our code by making it independent of things that are fragile, volatile, or out of our control. The idea of inverting dependencies is that our code should not adapt to details or concrete implementations, but rather the other way around: we want to force whatever implementation or detail to adapt to our code via a sort of API

* Details should depend on abstractions.

* Components should interact with interface rather than concrete implementation.

> It is often called **dependency injection**: because the dependency can be provided dynamically.

* It is better to use abstract base classes to define the behavior rather than using duck typing.

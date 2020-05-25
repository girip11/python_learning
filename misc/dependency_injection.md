# Dependency Injection

* With dependency injection, the client (who is in need of an object for its service ex: database client) can avoid knowing how to instantiate the object that it needs.

* By client getting the dependent object in its constructor/method, we can do unit testing easily by passing mock objects.

* Also if the dependent object needs to be changed (for instance from postgres to mariadb client) in the future, the client code still remains untouched.(open closed principle in SOLID)

## Various ways to inject dependencies

* Pass the dependency in constructor - Constructor Injection
* Pass the dependency to required method - Parameter Injection
* Set the dependency using setter property - Setter Injection

---

## References

* [Dependency Injection Myth: Reference Passing](http://misko.hevery.com/2008/10/21/dependency-injection-myth-reference-passing/)

* [Dependency injection code example](https://github.com/faif/python-patterns/blob/master/patterns/dependency_injection.py)

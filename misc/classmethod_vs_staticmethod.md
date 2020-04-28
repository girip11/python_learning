# Python's `@classmethod` and `@staticmethod` Explained

## `@classmethod` decorator

* Since the class method is passed the **cls** parameter which is the class object itself, it is commonly used for instantiating the class behaving like a class factory.

* Class methods can be useful in inheritance situations to instantiate subclasses as well.

* These methods can also be used to dynamically add some attributes to the classes since they have access to those objects.

```Python
class Myclass:
    @classmethod
    def from_string(cls, input_str):
        pass

    @classmethod
    def from_json(cls, input_json):
        pass
```

## `@staticmethod` decorator

* This method behaves as true static method similar to Java.
* No class(cls)or instance(self) parameter is implicitly passed to this method
* Class level utility methods are often stored in static methods.

```Python
class Myclass:
    @classmethod
    def from_string(cls, input_str):
        parsed = parse(input_str)
        # Myclass.validate is also fine. But does not go well
        # with inheritance situations
        cls.validate(parsed)
        pass

    @classmethod
    def from_json(cls, input_json):
        parsed = parse(input_json)
        cls.validate(parsed)
        pass

    @staticmethod
    def validate(args):
        pass
```

* Use static method when the logic can be extracted as a utility and that does not require to operator on a class object or the instance object.

* Common logic among multiple classmethods are good candidates to be made as a static method.

---

## References

* [Python's @classmethod and @staticmethod Explained](https://stackabuse.com/pythons-classmethod-and-staticmethod-explained/)

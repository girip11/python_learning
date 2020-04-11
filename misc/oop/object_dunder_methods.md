# Magic methods on object

> A class can implement certain operations that are invoked by special syntax (such as arithmetic operations or subscripting and slicing) by defining methods with special names. This is Python’s approach to operator overloading - [Special method names](https://docs.python.org/3/reference/datamodel.html#special-method-names)

## `__init__`, `__new__`,  `__call__` and `__del__`

* [`__new__`](https://docs.python.org/3/reference/datamodel.html#object.__new__) - controls the object creation. Instance can be created inside `__new__` method either by using `super()` or by directly calling `__new__` method over `object`, where if parent class is `object`.

> `__new__()` is intended mainly to allow subclasses of immutable types (like int, str, or tuple) to customize instance creation. It is also commonly overridden in custom metaclasses in order to customize class creation.

* [`__init__`](https://docs.python.org/3/reference/datamodel.html#object.__init__) is automatically called on the object returned by `__new__`
* If `__new__()` does not return an instance of **cls**, then the new instance’s `__init__()` method **will not be invoked**.
* `__init__` - controls the Object initialization

```Python
class SimpleAbstractClass:
    # cls is implicitly passed during construction
    # this method can return instance of other object
    # or already constructed object stored in a global variable
    def __new__(cls, *args, **kwargs):
        if cls == SimpleAbstractClass:
            raise Exception("Abstract class cannot be instantiated")
        return super().__new__(cls, *args, **kwargs)

class ConcreteClass(SimpleAbstractClass):
    def __init__(self):
        print("Inside the concrete class")

cc = ConcreteClass()
# raises exception
sc = SimpleAbstractClass()
```

* `__call__` - makes the [object callable](../../python3_oop/7_python_oo_shortcuts.md) and support function like invocation.

* [`__del__`(aka finalizer or destructor)](https://docs.python.org/3/reference/datamodel.html#object.__del__) - Called when the object is about to get garbage collected.

> `del x` doesn’t directly call `x.__del__()` — the former decrements the reference count for x by one, and the latter is only called when x’s reference count reaches zero.

## Custom getters and setters on attributes

* One way to associate getters and setters with an attribute is using the [`@property` decorator](../../python3_absolute_beginners/chapter_9_classes.md).

* Other way is to define `__getattr__` and `__setattr__`.  In cases where we can define attributes directly on the class **property decorator** approach is preferred.

* `__getattr__` and `__setattr__` could be useful in cases where the attributes are stored internally using a hash data structure or in some form that makes the **attribute not invoke directly on the object itself**.

```Python
class SimpleClass:
    def __init__(self, **kwargs):
        """
        Supported options are
        * host
        * port
        * protocol
        """
        # options are now stored as dict
        super().__setattr__("options", {})
        self.options = kwargs

    def __getattr__(self, attr_name):
        print(f"Getter called for {attr_name}")
        if attr_name in self.options:
            return self.options[attr_name]

        raise AttributeError(f"{type(self).__name__} does not have attribute {attr_name}")

    def __setattr__(self, attr_name, value):
        print(f"Setter called for {attr_name} with value {value}")

        self.options[attr_name] = value

sc = SimpleClass(host="example.com", port=8080, protocol="https")

print(sc.host)
print(sc.port)
sc.protocol = "http"
```

**NOTE** - Builtins `getattr` and `setattr` don't just call in to these magic methods like `len`.

> A class instance has a namespace implemented as a dictionary which is the first place in which attribute references are searched. When an attribute is not found there, and the instance’s class has an attribute by that name, the search continues with the class attributes. If a class attribute is found that is a user-defined function object, it is transformed into an instance method object whose `__self__` attribute is the instance. Static method and class method objects are also transformed; see above under “Classes”. See section Implementing Descriptors for another way in which attributes of a class retrieved via its instances may differ from the objects actually stored in the class’s `__dict__`. If no class attribute is found, and the object’s class has a `__getattr__()` method, that is called to satisfy the lookup.
> Attribute assignments and deletions update the instance’s dictionary, never a class’s dictionary. If the class has a `__setattr__()` or `__delattr__()` method, this is called instead of updating the instance dictionary directly.
>Class instances can pretend to be numbers, sequences, or mappings if they have methods with certain special names. See section Special method names.
>Special attributes: `__dict__` is the attribute dictionary; `__class__` is the instance’s class. - [Python data model](https://docs.python.org/3/reference/datamodel.html)

## Access attributes using dictionary like lookup (subscriptable)

## Iterators

---

## References

* [Special methods for object customization](https://docs.python.org/3/reference/datamodel.html#basic-customization)

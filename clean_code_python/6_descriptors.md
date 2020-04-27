# Descriptors

* Available from python 3.6+.

* **DescriptorClass** - implements the descriptor protocol. Descriptor protocol should contain the following methods.
  * `__get__`
  * `__set__`
  * `__delete__`
  * `__set_name__`
* **ClientClass** - contains an instance of the **DescriptorClass** as **its class attribute**.

* A client class can have any number of descriptors, with each descriptor mapping to an attribute of the client class.

```Python
# Basic code outline
class DescriptorClass:
    # implement all the descriptor protocol methods
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

    # This method was added in Python 3.6
    def __set_name__(self, owner, name):
        pass

class ClientClass:
    # Class attribute name for a descriptor can be anything
    descriptor = DescriptorClass()
    # A class can have many descriptors
    email = DescriptorClass()

client = ClientClass()

# This calls the descriptor's __get__ method
client.descriptor
```

## `__get__(self, instance, owner)`

* When we access the descriptor attribute from an instance of the **ClientClass**, instead of returning the descriptor object, the descriptor object's `__get__` magic method is called. This happens only when the class attribute object is a descriptor object.

* `__get__` method is called when the descriptor attribute is accessed from the class **ClientClass** and as well as any of the instances of the **ClientClass**.

* When accessed from the class, the **instance parameter** is set to `None`. When called from instance of the class, **instance parameter** is set to that instance and the owner will be class of the instance.

* **self** is commonly returned when the descriptor is accessed directly through the class.

## `__set__(self, instance, value)`

* This method is called when a value is assigned to the descriptor.

* This method similar to the `@property.setter` can be used to run validations before setting the value to the attribute.

**NOTE**: If the descriptor object does not have this method implemented, then assignment to the descriptor attribute will assign the value directly to it, thus overwriting the descriptor object itself.

## `__delete__(self, instance)`

* This method is called on `del client_instance.descriptor`.

## `__set_name__(self, owner, name)`

* Automatically called when creating the descriptor class attribute.

* Available from python 3.6 onwards. Previously name was explicitly passed through the DescriptorClass `__init__` method.

```Python
class DescriptorClass:
    # This is how name was set prior to the introduction of __set_name__
    def __init__(self, name=None):
        self.name = name

    # Automatically called
    def __set_name__(self, owner, name):
        self.name = name
    ...

class ClientClass:
    # This calls the magic method __set_name__ with email
    # as the name parameter.
    email = DescriptorClass()
```

## Types of descriptor

* Data descriptor - implements `__set__` or `__delete__` or both (along with or without `__get__`)
* Non data descriptor - implements only `__get__`

> When trying to resolve an attribute of an object, a data descriptor will always take precedence over the dictionary of the object, whereas a non-data descriptor will not. This means that in a non-data descriptor if the object has a key on its dictionary with the same name as the descriptor, this one will always be called, and the descriptor itself will never run. Conversely, in a data descriptor, even if there is a key in the dictionary with the same name as the descriptor, this one will never be used since the descriptor itself will always end up being called.

* In data descriptors, descriptor will always be called on get, set and delete actions over the object's dictionary.

> If the descriptor implements `__set__()`, then it will always take precedence, no matter what attributes are present in the dictionary of the object. If this method is not implemented, then the dictionary will be looked up first, and then the descriptor will run.
> Do not use `setattr()` or the assignment expression directly on the descriptor inside the `__set__` method because that will trigger an infinite recursion.
> We **cannot** use `getattr()` and `setattr()` on the descriptor attributes, so modifying the `__dict__` attribute is the last standing option.

**NOTE**- Refer the book for detailed explanations on data and nondata descriptor.

## Descriptor applications

> Do not implement a descriptor unless there is actual evidence of the repetition we are trying to solve, and the complexity is proven to have paid off.
> Descriptors are more appropriate for defining libraries, frameworks, or internal APIs, and not that much for business logic.

* Descriptors can also be applied when we need to store data that is common to all the instances of a class.

## Using weak references instead of `__dict__`

This approach is **not recommended**. We will encounter following undesirable things when using weak references.

* Attributes with descriptor objects and not with the client objects
* All client objects should be hashable.

## Descriptor Uses

### Reusing code

> The best way to decide when to use descriptors is to identify cases where we would be using a property (whether for its get logic, set logic, or both), but repeating its structure many times.

* Descriptors can be used with decorators to make them work with functions as well as instance methods.

> In general, descriptors will contain implementation logic, and not so much business logic.

### Descriptors can replace class decorators

Example in the book explains it nicely.

## Analysis of descriptors

Refer the book for analysis of descriptors

> In this line, we have suggested that we should reserve the functionality of descriptors for truly generic cases, such as the design of internal development APIs, libraries, or frameworks. Another important consideration along these lines is that, in general, we should not place business logic in descriptors, but rather logic that implements technical functionality to be used by other components that do contain business logic.

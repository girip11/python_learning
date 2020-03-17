# OOP basics in Python

* A type and its instances are objects in python. `vars` dumps the attributes on an object.
* `vars(type)` dumps class level attributes while `vars(instance)` dumps attributes that belong to that instance.

```Python
from typing import ClassVar

class SimpleClass:
    # This class variable
    class_var: ClassVar[int] = 100

    def __init__(self, arg):
        self.data = arg

# SimpleClass type is also an object in python
# This will not contain the instance level attribute data
print(vars(SimpleClass))

# attributes on the instance
# This will not contain the class level attribute class_var
print(vars(SimpleClass(100)))
```

## Empty class and dynamic attribute addition

* To objects of a class, we can add attributes dynamically.

* By **assigning values to attributes that doesnt** already exist on the object, that attribute gets added to that object with the value assigned.

```Python
# This is an empty class
class EmptyClass:
    pass

eo1 = EmptyClass()

# dumps the instance variables of the object eo1. It is a dictionary
print(vars(eo1)) # prints {}

eo1.data = 100

# prints { "data": 100 }
# This attibute is available only on the object eo1
# If another object on EmptyClass is created, it won't be containing this
# data attribute.
print(vars(eo1))

eo2 = EmptyClass()

# prints {}
print(vars(eo2))

# This would raise AttributeError
print(eo2.data)
```

* These dynamic attributes will only be available to that object, other objects of the same class will not contain that attribute. Trying to access those attributes on other objects will raise `AttributeError`.

* If we need to check if an attribute is present in an object gracefully, we can use the `getattr(object/type/module, attr_name, default)` method. This can fetch methods on a module, properties on methods on type and object. When the default parameter is provided no exception is raised when the attribute is not found.

* Dynamic attributes can also be set on an object using the `setattr` method.

```Python
class EmptyClass:
    pass

eo1 = EmptyClass()
print(vars(eo1)) # prints {}

setattr(eo1, "Name", "John Doe")
print(vars(eo1))
```

## Class attributes and instance attributes

* Class level attributes **can be accessed** via the class name as well as through the instances, but **can only be modified using the class name**.

* If class level attribute is accessed via object and assigned some other value, it does not change the value of the class variable, instead creates a new dynamic attribute on that object. This could introduce unintended bugs. Hence it is always **recommended to access the class variable through the class name**

* Add the **type hint** `ClassVar` if the variable is intended to be used as class variable. Omit the type hint if the variables are to be used as instance variables.

```Python
from typing import ClassVar

class SimpleClass:
    # This class variable
    class_var: ClassVar[int] = 100

    def __init__(self, arg):
        self.data = arg

    @staticmethod
    def say_hello():
        print("Hello")

# contains the class level attribute class_var
print(vars(SimpleClass))
print(f"SimpleClass.class_var:{SimpleClass.class_var}")

simple_obj1 = SimpleClass(100)
# Notice the object does not have attribute class_var
print(vars(simple_obj1))
# But still we can access the variable value through the object
print(f"simple_obj1.class_var:{simple_obj1.class_var}")

# This will not change the value of the class variable. Instead this
# will create new attribute class_var on the simple_obj1
simple_obj1.class_var = 10
print(vars(simple_obj1))
# class level variable is untouched
print(vars(SimpleClass))

print(f"SimpleClass.class_var:{SimpleClass.class_var}")
# Here instance level attribute is accessed
print(f"simple_obj1.class_var:{simple_obj1.class_var}")
```

* If we need to declare instance variables outside of all the methods but inside the class similar to the way class variables are used we can either user [**dataclass**](../python_data_classes.md) from `dataclasses` module or **NamedTuple** from `typing` module.

## Listing all attributes and methods on classes and objects

* `dir(type_or_obj)` - prints all the attributes(includes methods and magic methods) of the type or the object.

* Using this we can iterate through the attributes of the object.

```Python
from typing import ClassVar

class SimpleClass:
    # This class variable
    class_var: ClassVar[int] = 100

    def __init__(self, arg):
        self.data = arg

    @staticmethod
    def say_hello():
        print("Hello")

print(dir(SimpleClass))

print(dir(SimpleClass(100)))
```

## Creating class dynamically and instantiating

* `type(obj1) is type(obj2)` - compares if the objects are instances of same type.

* `type(type_name, (bases_tuple), {attribute_dict})` - creates a new type and returns an object of that type.

```Python
dynamic_obj1 = type('DynamicClass', (), {'data': 100})
print(vars(dynamic_obj1))
print(dynamic_obj1.data)

dynamic_obj2 = type('DynamicClass', (), {'data': 1000})
print(vars(dynamic_obj2))
print(dynamic_obj2.data)

# comparing type of objects
print(type(dynamic_obj1) is type(dynamic_obj2))
```

## Object cloning, shallow copy and deep copy

* Multiple aliases to the same object can be created using the assignment operator.

```Python
numbers = [1, 2, 3, 4, 5]

# ranks now is an alias for objects pointed by numbers
ranks = numbers

print(ranks is numbers)
ranks.append(6)

print(numbers)
```

* Object cloning (shallow copying) by copying the `__dict__` attribute. Better way to clone objects is to use the `copy` module.

```Python
class SimpleClass:
    def __init__(self):
        self.data = [1, 2, 3]

sc1 = SimpleClass()
sc1.data.append(100)


sc2 = SimpleClass()
# This does a shallow cloning
sc2.__dict__.update(sc1.__dict__)

# True - both lists are same objects
print(sc1.data is sc1.data)
```

### `copy` module

* Shallow copy - creates a new object, but the inner objects of the cloned object and the original object share the references.

```Python
import copy

country_list = {
    "a": ["Australia", "Austria"],
    "b": ["Brazil"]
}

# shallow copy
shallow_country_list = copy.copy(country_list)

# False because two different objects
print(shallow_country_list is country_list)

# Prints True
print(shallow_country_list["a"] is country_list["a"])

# This will get reflected in the original country_list object
# since inner objects share the same references in shallow copy.
shallow_country_list["b"].append("Bangladesh")

print(shallow_country_list["b"])
print(country_list["b"])
```

* Deep copy - Object is cloned recursively including the inner objects.

```Python
# Deep copy
deep_country_list = copy.deepcopy(country_list)

# False because two different objects
print(deep_country_list is country_list)

# Prints False. Inner objects are also cloned
print(deep_country_list["a"] is country_list["a"])

deep_country_list["a"].append("Afghanistan")
print(deep_country_list["a"])
print(country_list["a"])
```

---

## References

* [OOP Programming examples](https://www.pythonprogramming.in/object-oriented-programming.html)

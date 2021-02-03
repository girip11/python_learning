# Classes

## Creating and instantiating class

* Any attribute or method prefixed with an underscore **should not be** accessed from outside the class.
* Any attribute or method prefixed with double underscores(dunder) will make the attribute/method private to that class/instance.(This is achieved through **name mangling** and can be verified using the `dir(class/instance)`)

```Python
class Employee:
    def setName(self, name):
        # name is considered private attribute
        self.__name = name.title()

    def getName(self):
        return self.__name

    def setAge(self, age):
        self._age = age

    def getAge(self):
        return self._age

    def setDesignation(self, designation):
        self.__designation = designation.title()

    def getDesignation(self):
        return self.__designation

# instantiating a class
employee1 = Employee()
employee1.setName("John Doe")
employee1.setAge(25)
employee1.setDesignation("Software Engineer")

# Observe name mangling for attributes __name and __designation
dir(employee1)

# We can access _age from outside, but it is not recommended in python
print(employee1._age)

# __name and __designation cannot be accessed directly from outside
print(employee1.__name) # name mangled to _Employee__name
print(employee1.__designation) # name mangled to _Employee__designation

# accessing attributes directly
print(",".join([employee1.name, str(employee1.age),
employee1.designation]))

# accessing through getters
print(",".join([employee1.getName(), str(employee1.getAge()),
employee1.getDesignation()]))
```

## `self`

`self` refers to the object on which the method is operating. `dir(instance)` returns list of names available within that object.

## Object identity

Object assigned an identity when created. `id()` builtin function returns the object id. To compare two objects we can use the **is** operator.

```Python
employee1 = Employee()
employee1.setName("John Doe")
employee1.setAge(25)
employee1.setDesignation("Software Engineer")

employee2 = Employee()
employee2.setName("Jane Doe")
employee2.setAge(25)
employee2.setDesignation("Software Engineer")

print(id(employee1))
print(id(employee2))

print(employee1 is employee2)
```

object id is an integer. Every object has unique id.

## Object type

`type(instance)` builtin returns the typeof the object.

**NOTE**: **type** and **id** are used only for debugging purposes. `type` can also be used for creating a class dynamically (metaprogramming)

## Namespaces

Each object has its own namespace dictionary. Names are added to object namespace when first assignment to the variable is done or when a module is imported. This is called **name binding**. Scope is the visibility of a name inside a code block
Names defined inside a class definition can be accessed inside its methods only through **self**. Names are looked up in the scope of the current class before proceeding to search in the scope of its base classes. `NameError` raised when the name is not found in any scope.

## Inheritance

```Python
# we can refer to this relationship as
# parent class, child class or
# base class, derived class or
# super class , subclass

# Syntax
class Parent:
  # parent class body

class Child(Parent):
  # child class
```

## Magic methods

These methods are part of programming languages. These method names are flanked on both sides by double underscores.

## Constructors

`object.__init__(self, params...)`. Constructor does not return any values.

```Python
class Employee:
    def __init__(self, name, gender, designation):
        self.name = name
        self.gender = gender
        self.designation = designation

# object creation
employee1 = Employee("Jane Doe", "Female", "Software Engineer")
```

The constructor of the base class can be called from the derived class constructor using the `super()` function. We can call any overridden method of the base class from the overriding method in the derived class using the `super()` function.

```Python
# Child class constructor usually calls parent class constructor.
class Parent:
    def __init__(self, param1, param2):
        # constructor code

class Child1(Parent):
    def __init__(self, param1, param2, param2):
        # This is one way of calling parent constructor. Alternate way is calling user super() which is preferred over this way.
        # this syntax is very useful in mutliple inheritance scenarios, where we have to call __init__ of two or more parents of the child class
        Parent.__init__(self, param1, param2)
        self.param3 = param3

class Child2(Parent):
    def __init__(self, param1, param2, param2):
        super().__init__(param1, param2)
        self.param3 = param3
```

## String representation of the object

String representation of an object can be customized using the method `object.__str__(self)`. This methods is used by the builtins `str(object)` and `print(object)`

The `print()` and `str()` built-in function uses `__str__` to display the string representation of the object while the `repr()` built-in function uses `__repr__` to display the object.

**NOTE**: `str()` is used for creating output for end user while `repr()` is mainly used for **debugging and development**. `repr()` goal is to be **unambiguous** and `str()` is to be **readable**.

> Implement `__repr__` for any class you implement. This should be second nature. Implement `__str__` if you think it would be useful to have a string version which errs on the side of readability. [Stackoverflow: `str()` vs `repr()`](https://stackoverflow.com/questions/1436703/difference-between-str-and-repr)

```Python
# Child class constructor usually calls parent class constructor.
class Parent:
  def __init__(self, param1, param2):
    # constructor code

class Child(Parent):
    def __init__(self, param1, param2, param2):
        super().__init__(param1, param2)
        self.param3 = param3
  
    # used by str() and print() builtins
    # informal string representation
    def __str__(self):
        return """{0}, {1}, {2}""".format(self.param1, self.param2, self.param3)

    # official string representation. used by repr() builtin
    def __repr__(self):
        return """Child({param1!r}, {param2!r}, {param3!r})""".format(**vars(self))

child = Child("arg1", "arg2", "arg3")
print(child)
print(str(child))
print(repr(child))
```

## Properties

`property([fget], [fset], [fdel], [doc])`

All four parameters optional. If none provided, makes the attribute inaccessible. The actual attribute name is **prefixed with double underscores**. Property takes the name of the attribute without the double underscores.

* read_only property - `property(get_function)`
* read/write property - `property(get_function, set_function)`. These methods are invoked on every read or write to the property.
* delete the attribute - third argument. keyword arguments supported, which means we can only specify delete parameter and skip other ones.`property(fdel = del_function)`
* docstring for the property - fourth argument. `property(doc = docstring)`

```Python
class Planet:

    def __init__(self, name):
        self._name = name

    def get_position(self):
        """
            Position of the planet from the Sun
        """
        return self._position

    def set_position(self, position):
        if position > 0:
            self._position = position
        else:
            raise ValueError("position should be greater than 0")

    position = property(get_position, set_position)


earth = Planet("Earth")
earth.position = 3

print(earth.position)
help(earth.get_position)

```

Drawback with the above method is we can set the position of the planet in two ways,

* `planet.position = 3` and
* `planet.set_position(3)`

This violates **Zen of Python** principle **"There should be one and preferably only one obvious way to do it"**. We could make the getter and setter methods private by prefixing with **double underscore(dunder)**, but using the [`@property` approach is considered as the pythonic way](https://www.python-course.eu/python3_properties.php).

* Python property using decorators.

This syntax is preferred compared to using the `property()` function.

```Python
class Planet:

    def __init__(self, name):
        self._name = name

    @property
    def position(self):
        """
            Position of the planet from the Sun
        """
        return self._position

    @position.setter
    def position(self, position):
        if position > 0:
            self._position = position
        else:
            raise ValueError("position should be greater than 0")

    @position.deleter
    def position(self):
        del self._position


earth = Planet("Earth")
earth.position = 3
# prints _position
dir(earth)

print(earth.position)
del earth.position

# prints without _position
dir(earth)
```

## Customizing attribute access

* These methods are invoked when an attribute is called on an object using the dot notation. `obj.my_attr` calls `__getattr__` on the object `obj` passing name of the attribute `my_attr` as the parameter.

* `object.__getattr__(self, name)` - returns attribute value.
* `object.__setattr__(self, name, value)` - on attribute assignment attempt
* `object.__detattr__(self, name)` - on deleting the attribute.

These methods are invoked on the object when called using the builtins `getattr`, `setattr` and `delattr` respectively.

**NOTE**: understand with examples  on usage of attribute, property, magic method(__getattr__).

## Other useful magic methods for emulating containers (list, dictionary)

* `object.__len__(self)`- returns length of the object as integer. used by the builtin `len()` method.
* `object.__getitem__(self, key)`- should return value similar to output of `self[Key]`
* `object.__setitem__(self, key, value)`- should set value when accessed like `self[Key]`
* `object.__delitem__(self, key)`- similar to using with **del** statement.
* `object.__iter__(self)` - iterating purpose
* `object.__reversed__(self)` - invoked by `reversed()` builtin function.
* `object.__contains__(self, item)` - contains operation.

## Class Attributes

Class attributes are defined outside of all the methods, usually they are placed at the top, right below the class header. Class attributes can be accessed using `ClassName.AttributeName`. It is **not recommended to access** the class attributes through the instances.

```Python
class SimpleClass:
    instance_count = 0

    def __init__(self, arg):
        self.arg = arg
        SimpleClass.instance_count += 1

print(SimpleClass.instance_count)
ins1 = SimpleClass('foo')
ins2 = SimpleClass('bar')
print(SimpleClass.instance_count)

# class attributes can also be accessed via the instances
print(ins1.instance_count)
print(ins2.instance_count)

# Class and instance attributes are stored in
# separate dictionaries accessed using `__dict__`
print(SimpleClass.__dict__)
print(ins1.__dict__)

# reset instance count
SimpleClass.instance_count = 0
```

## Static Methods

`@staticmethod` decorator added directly in front of the method header makes the method a static method

```Python
class SimpleClass:
    __instance_count = 0

    def __init__(self, arg):
        self.arg = arg
        # SimpleClass.instance_count += 1
        # Below syntax can only be used in instance methods
        type(self).__instance_count += 1 # alternate way to access the class attributes

    @staticmethod
    def Instances():
        # Notice we have to hardcode the classname to
        # refer to the class attribute inside a static method.
        return SimpleClass.__instance_count

print(SimpleClass.Instances)
ins1 = SimpleClass('foo')
ins2 = SimpleClass('bar')
print(SimpleClass.Instances)

# static methods can also be accessed via the instances
print(ins1.Instances)
print(ins2.Instances)
```

**NOTE**: If we were to refer to class attributes inside a **static method**, we would have to hardcode the name of the class inside the static method. This might create problems when the class is inherited and used inside derived classes. To handle such cases, [**static methods can be used alongwith the class methods**](https://www.python-course.eu/python3_class_and_instance_attributes.php).

## Class methods

* Class method is bound to a class. Declared using the `@classmethod` decorator.
* First parameter to the class method is always the reference to the class.
* Very useful in inheritance scenario where we need to access information related to the class on which the method was called.

```Python
class Editor:
    _description = "I am a normal text editor"

    @classmethod
    def description(cls):
        print(cls._description)

class PythonEditor(Editor):
    _description = """
    I am a text editor with Python syntax highlighting capabilities
    """

class RubyEditor(Editor):
    _description = """
    I am a text editor with Ruby syntax highlighting capabilities
    """

Editor.description()
PythonEditor.description()
RubyEditor.description()

```

**NOTE**: Static methods are often invoked from class methods, so that static methods can be generic and the class specific information can be passed from the class method to the static method.

---

## References

* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)

* [Property vs __getattr__](https://stackoverflow.com/questions/22616559/use-cases-for-property-vs-descriptor-vs-getattribute)

* [Python Properties vs Getters and setters](https://www.python-course.eu/python3_properties.php)

* [Class Methods vs. Static Methods and Instance Methods](https://www.python-course.eu/python3_class_and_instance_attributes.php)

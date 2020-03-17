# Encapsulation in Python

## Private attributes

* To make an attribute private to the class, prefix it with **double underscores**. In python any identifier prefixed with double underscores (only when prefixed) will be subjected to name mangling.

* This comes very handy in inheritance, where we wanted the attribute access exclusive to the class.

```Python
class Parent:
    def __init__(self):
        print("Inside parent class init")
        self.__private_var = "Parent private var"

    def get_private_var(self):
        print(f"From Parent.get_private_var, Instance type: {type(self)}")
        # variable lookedup is __Parent_private_var always
        return self.__private_var

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child class init")
        # This is a variable exclusive to Child class instance
        self.__private_var = "Child private var"

    def get_my_private_var(self):
        # If the child does not have this __private_var
        # defined, this statement will raise AttributeError
        print(f"From Child.get_my_private_var, Instance type: {type(self)}")
        # Variable lookup is _Child__private_var
        return self.__private_var

    def get_parent_private_var(self):
        # will raise error because the below will lookup
        # _Child__private_var in its parent namespace which wont
        # be found.
        return super().__private_var

parent = Parent()
# prints {'_Parent__private_var': 'Parent private var'}
print(vars(parent))
print(parent.get_private_var())

c = Child()
dir(c)

# prints 'Child private var'
print(c.get_my_private_var())

# prints "From Parent.get_private_var, Instance type: <class '__main__.Child'>"
# prints 'Parent private var'
print(c.get_private_var())

# prints "From Parent.get_private_var, Instance type: <class '__main__.Child'>"
# prints 'Parent private var'
print(c.get_parent_private_var())
```

* In the above example, when instance variable `__private_var` is accessed through the method of the parent class `get_private_var` either directly or indirectly from the child class instance, we are able to access the `__private_var` of the `Parent`. **Name mangling uses the class name of the method from which we are accessing the variable irrespective of the type of the instance.**.

* If the `_private_var` is accessed from one of the methods inside the `Child` class, a variable with the name `_Child__private_var` is searched in its namespace as well as its parent namespace. If no such variable is found, raises `AttributeError`
* If the `_private_var` is accessed from one of the methods inside the `Parent` class (via Parent class instance or instance of its subclass), a variable with the name `_Parent__private_var` is searched in its namespace as well as its parent namespace. If no such variable is found, raises `AttributeError`

## Protected Attributes

* To make an attribute protected, prefix the name with **single underscore**

```Python
class Parent:
    def __init__(self):
        print("Inside parent class init")
        # This attribute will be inherited by subclasses
        self._protected_var = "protected var set by Parent"

    def get_protected_var(self):
        print(f"From Parent.get_protected_var, Instance type: {type(self)}")
        return self._protected_var

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside child class init")

    def set_protected_var(self):
        print(f"From Child.set_protected_var, Instance type: {type(self)}")
        self._protected_var = "protected var set by Child"

    def get_child_protected_var(self):
        return self._protected_var

parent = Parent()
print(vars(parent))
print(parent.get_protected_var())

c = Child()
print(dir(c))
print(vars(c))

# both should yield same value
# "protected var set by Parent"
print(c.get_child_protected_var())
print(c.get_protected_var())

c.set_protected_var()

# Both should print same value
# "protected var set by Child"
print(c.get_child_protected_var())
print(c.get_protected_var())
```

---

## References

# Making choices

## `is` operator

* `==` - compares for equality in value.

```Python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

* `is` operator checks if both the variables point to the same object by comparing the object identities

```Python
a = [1, 2, 3]
b = list(a)

# False
print(a is b)
print(f"ID of a: {id(a)}, ID of a: {id(b)}")

# Now both the variables point to the same object.
a = b
print(a is b)
print(f"ID of a: {id(a)}, ID of a: {id(b)}")
```

* Commonly used to compare variable with **None**

```Python
def assign_role():
    import random
    return random.choice(["operator", None])

role = assign_role()

if role is not None:
    print(role)

a = "Hello"
b = "Hello"

print(a == b)
# This shows python maintains a single copy of the string literals
print(a is b)
```

---

## References

* [Python is operator](https://dbader.org/blog/difference-between-is-and-equals-in-python)
* [Python3 for absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)

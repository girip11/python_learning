# Prebound method pattern

In a module we can instantiate a top level class and assign the methods of that object to global variables in that module for the ease of access to the client modules.

```Python
# snippet from random module
from datetime import datetime

class Random8(object):
    def __init__(self):
        self.set_seed(datetime.now().microsecond % 255 + 1)

    def set_seed(self, value):
        self.seed = value

    def random(self):
        self.seed, carry = divmod(self.seed, 2)
        if carry:
            self.seed ^= 0xb8
        return self.seed

_instance = Random8()

# This is where we assign object methods to the module global variables
random = _instance.random
set_seed = _instance.set_seed
```

* Such pattern is used in random module in python's standard library as well as in the calendar module.

---

## References

* [The Prebound Method Pattern](https://python-patterns.guide/python/prebound-methods/)

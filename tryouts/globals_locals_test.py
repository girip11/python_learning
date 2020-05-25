# References:
# https://stackoverflow.com/questions/5354676/how-can-i-add-attributes-to-a-module-at-run-time

"""
This module uses the globals_locals.py module and tries to add some global
state to the module during runtime.
"""

import sys

from tryouts import globals_locals

print(f"1. Names present in the global_locals_test module: {globals()}")

print(
    "Creating a global attribute called Bar in globals_locals from the globals_locals_test"
)

setattr(globals_locals, "Bar", "10")

# Compare the two dirs to see if they share the same global state
# They both will be the same.
# This concludes the imported module is a singleton object.
# If its state is modified from any other modules, all other modules
# using that module can see the change.
print(dir(globals_locals))

print(dir(sys.modules["tryouts.globals_locals"]))

print(f"Value of Bar as seen from globals_locals.Bar:{globals_locals.Bar}")


# After adding the attribute to the module, import the attribute
# Importing this way creates a local copy of Bar in the attribute dictionary of
# this module
from tryouts.globals_locals import Bar

print(
    f"2. names present in the global_locals_test module after importing Bar: {globals()}"
)

print(f"Value of Bar as seen directly from globals_locals_test after import:{Bar}")

print(
    """Modifying the value of Bar on globals_locals will not affect this module because
this module contains a local copy of that value imported in to its dictionary"""
)

globals_locals.Bar = 100

print(f"globals_locals.Bar = {globals_locals.Bar}, Bar={Bar}")

# ensure current workspace directory is added to PYTHONPATH
# so that the tryouts package will be found and simple_package subpackage
# will be imported
# We can use only absolute namespace since we use this as __main__ module
from tryouts import simple_package

simple_package.a.foo()
simple_package.b.bar()

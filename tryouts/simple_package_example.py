# ensure current workspace directory is added to PYTHONPATH
# so that the tryouts package will be found and simple_package subpackage
# will be imported
# We can use only absolute namespace since we use this as __main__ module
from tryouts import simple_package

simple_package.a.foo()
simple_package.b.bar()


def say_hello(name: str) -> None:
    """Print hello to the console.

    Arguments:
        name {str} -- Name of the person to say hello to
    """
    print(f"Hello, {name}")


say_hello("John")

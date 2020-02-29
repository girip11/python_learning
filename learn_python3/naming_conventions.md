# Python Naming Conventions

## [Naming conventions](https://medium.com/better-programming/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841)

* camelCase
* PascalCase (aka CamelCase or upper camel case)
* snake_case
* kebab-case (This style is often used in URLs.)

## General

* Names should not be too small or too verbose.
* All letters of abbreviations should be capitalized in PascalCase. Ex: **HTTPServer**

## Packages, Modules

* Follows **snake_case**
* Its preferrable (not mandatory) to give packages **1 word name**

## Constants, Global Variables, Class and Instance variables

* Constants follow **SNAKE_CASE** (all letters capitalized)

* Global and instance variables follow **snake_case**.

* Names of module private global variables and non public (protected) instance/class variables starts with an **underscore**

* If the name of the class/instance variable needs to be **mangled** to make the variable private(**makes it difficult to access the variable using just the variable name giving it a private type feel**), then the name is prefixed with **double underscores**

## Functions, Methods, Method arguments

* Follow **snake_case**

* Names of module private functions or non public class/static/instance methods (protected, private) are prefixed with **single underscore**

* If the method name needs to be mangled (private to the Class or the Object), then the name is **prefixed with double underscores**

* In case of instance methods, the first argument is named as **self** and in case of **class methods(not static methods)** the first argument is named as **cls** by convention.

* In case we need to force the arguments of a function or method to be positional only, we can prefix the argument names with double underscore which causes the argument names to be mangled and **hence making it difficult to be used as keyword arguments**.

**NOTE**: Identifiers of the form `__<name>__` are reserved in python. User defined identifiers should never follow this format. Otherwise it could create problems with future releases of python if the same name is being used for a magic method in future releases of python.

## Naming guidelines

> * Always try to use the most concise but descriptive names possible.
> -[Python PEP8](https://realpython.com/python-pep8/)

## Code Layout

* Surround top-level functions and classes with **two blank lines**.
* Surround method definitions inside classes with a **single blank line**.
* Use blank lines sparingly inside functions to show clear steps.

## Breaking code by line length

* Keep line length to 79 characters. Python will assume line continuation(implied continuation) if code is contained within parentheses, brackets, or braces. If it is impossible to use implied continuation, then you can use backslashes to break lines instead.

* If line breaking needs to occur around binary operators, like + and *, it should occur before the operator. This rule stems from mathematics. Mathematicians agree that breaking before binary operators improves readability.

* Use 4 consecutive spaces to indicate indentation.

* Prefer spaces over tabs. **Python 3 does not allow mixing of tabs and spaces**

* When you write PEP 8 compliant code, the 79 character line limit forces you to add line breaks in your code. To improve readability, you should indent a continued line to show that it is a continued line. There are two ways of doing this. The first is to align the indented block with the opening delimiter. The second is to use a hanging indent. You are free to chose which method of indentation you use following a line break.

## Closing braces

```Python
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
    ]

```

OR

```Python
list_of_numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
```

## Comments

* Limit the line length of comments and docstrings to 72 characters
* Use block comments to document a small section of code
* Use inline comments sparingly.

### Block comments

* Indent block comments to the same level as the code they describe.
* Start each line with a # followed by a single space.
* Separate paragraphs by a line containing a single #.

### Docstrings

* Surround docstrings with three double quotes on either side, as in """This is a docstring""".
* Write them for all public modules, functions, classes, and methods.
* Put the """ that ends a multiline docstring on a line by itself.
* For one-line docstrings, keep the """ on the same line.

## Whitespaces

## Programming recommendations

* Don’t compare boolean values to True or False using the equivalence operator.
* Use the fact that empty sequences are **False** in `if` statements
* Use `is not` rather than `not ... is` in if statements
* Don’t use `if x:`(checks if x is truthy) when you mean `if x is not None`
* Use `.startswith()` and `.endswith()` instead of **slicing**

## Tools

* Flake8
* Pylama

### Linters

* Pylint
* Pycodestyle
* Pydocstyle -docstring conventions
* Pyflakes - faster compared to pylint

### AutoFormatters

Formats the code to follow PEP 8 style guide.

* Black
* Autopep8
* YAPF

## Logical linting

* Bandit - common security issues.
* Mypy - static type checking

---

## References

* [Python Naming Conventions](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html)
* [Python PEP8](https://realpython.com/python-pep8/)
* [Python code quality tools](https://realpython.com/python-code-quality/)

# Learning Python3

If you are completely new to programming, then may be start learning python from [w3schools](https://www.w3schools.com/python/default.asp). Once done with this tutorial, start learning the below mentioned resources.

Familiar with atleast one object oriented programming language, then use the following references/books.

## Online resources

* I highly recommend [**Python Course**](https://www.python-course.eu/python3_history_and_philosophy.php)  
or
* [Python Course from dataflair](https://data-flair.training/blogs/python-tutorials-home/)

* [python-textbok](https://python-textbok.readthedocs.io/en/1.0) or [MIT notes](https://www.cs.uct.ac.za/mit_notes/python/)

## Books

* [Python3 for Absolute beginners](https://www.amazon.in/Python-Absolute-Beginners-Tim-Hall/dp/1430216328)

Once you are familiar/comfortable with python programming, then read the below books in the mentioned order to become a good python programmer.

* [Python3 Object oriented programming](https://www.amazon.in/dp/B005O9OFWQ/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)
* [Fluent Python](https://www.amazon.in/Fluent-Python-Luciano-Ramalho/dp/1491946008)
* [Effective Python](https://effectivepython.com/)

Other useful resources

* [Python Anti-patterns](https://docs.quantifiedcode.com/python-anti-patterns/)
* [Python tricks: A buffet of awesome python features](https://www.amazon.in/dp/B0785Q7GSY/ref=dp-kindle-redirect?_encoding=UTF8&btkr=1)


## VSCode IDE setup

### Mypy static type checking

* After installing all the dev dependencies, for the **mypy** vscode extension to work, install the **mypyls** (MyPy Language server) in to the pipenv provided virtual environment.

```bash
pipenv shell
pip install "https://github.com/matangover/mypyls/archive/master.zip#egg=mypyls[default-mypy]"
```

**NOTE**: If you update the mypy-vscode extension, you may also need to update the mypy language server separately. Do so by running the following command.

```Bash
pip install -U "https://github.com/matangover/mypyls/archive/master.zip#egg=mypyls[default-mypy]"
```

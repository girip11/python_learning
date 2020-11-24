# Python virtual environments

Virtual environments: isolated independent environments that can have both a specific version of Python and of any project-specific packages installed within them, without affecting any other projects.

## Installing multiple Python versions

For installing different python versions (for instance, python 2.7 and 3.6), use `pyenv` (think of it like rbenv in ruby).

```bash
# pyenv dependencies
deps='curl git gcc make zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev libssl-dev'

sudo apt-get update
sudo apt-get install -y $deps

# Installs pyenv to $HOME/.pyenv
curl https://pyenv.run | bash

# Add the below lines to the home directory .bashrc
echo 'export PATH="/home/vagrant/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

source ~/.bashrc

# check the pyenv version
pyenv --version

# To check python versions installed using pyenv
pyenv versions

# List python versions available for installing
pyenv install --list

# install a perticular python version
pyenv install 3.6.8
pyenv install 3.8.0

# check installed versions
pyenv versions

# set a global version
pyenv global 3.6.8

# check if the version is set
pyenv global
python --version
python3 --version

# should print ~/.pyenv/shims directory
which python
which python3

# create a local directory to work with python 3.8
mkdir python-3.8-sample && cd python-3.8-sample

# set the python version for this directory to 3.8.0
pyenv local 3.8.0

# check if the version is set
python3 --version

# `ls -al` in the current directory
# we should find a .python-version file
cat .python-version
```

**pyenv** looks in four places to decide which version of Python to use, in priority order:

* The `PYENV_VERSION` environment variable (if specified). You can use the pyenv shell command to set this environment variable in your current shell session.

* The application-specific `.python-version` file in the current directory (if present). You can modify the current directory's `.python-version` file with the pyenv local command.

* The first `.python-version` file found (if any) by searching each parent directory, until reaching the root of your filesystem.

* The global version file. You can modify this file using the pyenv global command. If the global version file is not present, pyenv assumes you want to use the "system" Python. (In other words, whatever version would run if pyenv weren't in your PATH.)

## Virtual environment for Python version >=3.3

* Python3 starting from **version 3.3** ships with **venv** for creating virtual environments. It is recommended to use **venv** on python versions >=3.3

```bash
# python3 -m venv <virtual_env_dir>
# convention is to use venv directory for virtual environments
python3 -m venv venv

# activate the venv
source venv/bin/activate

# after this any pip install command will be installed packages to venv directory

# deactivating
deactivate
```

## Virtual environment for Python version < 3.3

### Using **virtualenv**

* For **python versions < 3.3**, **virtualenv** can be used for creating virtual environments.

```bash
# Reference: https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b

# install pipfirst
sudo apt-get install python3-pip

pip3 install --user virtualenv

# create virtual environment
virtualenv venv

# virtual env using python 2.7 interpreter
virtualenv -p /usr/bin/python2.7 venv

# virtual env using python3 interpreter
virtualenv -p python3 venv

# activate virtual env
source venv/bin/activate

# deactivate the virtual env
deactivate
```

### Using **pyenv-virtualenv**

**pyenv-virtualenv** is a tool to create virtual environments integrated with pyenv, and works for all versions of Python.

> It is a **plugin** for **pyenv** by the same author as pyenv, to allow you to use pyenv and virtualenv at the same time conveniently - [venv-pyvenv-pyenv-virtualenv](https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe).

* Add the below line to ~/.bashrc to initialize this plugin.

```bash
eval "$(pyenv virtualenv-init -)"
```

This plugin is particularly very useful when managing python2.x environments (can also manage python3.x environments). Creating and managing virtual environments using **pyenv-virtualenv**

```bash
# pyenv virtualenv <python_version> <virtualenv_name>
pyenv virtualenv 2.7.10 my-virtual-env

# list all virtualenvs
pyenv virtualenvs

# pyenv activate <virtualenv_name>
pyenv activate my-virtual-env

# deactivate
pyenv deactivate

```

---

## **pipenv** for Application Dependency Management

> Pipenv is a dependency manager for Python projects. If you’re familiar with Node.js’ npm or Ruby’s bundler, it is similar in spirit to those tools. - [Python Docs: Virtualenvs](https://docs.python-guide.org/dev/virtualenvs/)

* [Pipenv](https://pypi.org/project/pipenv/) aims to combine **Pipfile, pip and virtualenv** into one command on the command-line.

* Use [Pipenv to manage library dependencies](https://packaging.python.org/guides/tool-recommendations/#application-dependency-management) when developing Python applications.

```bash
# Reference: https://docs.python-guide.org/dev/virtualenvs/
pip3 install --user pipenv

# add pip packages inside USER HOME directory to path
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# creates a Pipfile in current directory
pipenv install requests

# run python file
# very similar to ruby bundler
pipenv run python main.py
```

* Any project that has **Pipfile** can have its dependencies installed in the virtual environment using `pipenv install` command.

* By default pipenv will
  * always install the newest versions of packages.
  * will ONLY install the base packages that **are required in production**

* Along with the creation of **Pipfile**, **Pipfile.lock** is also created which contains exact versions of the dependency packages installed (Very similar to Gemfile.lock in ruby bundler ecosystem).

Following commands help in installing dependencies

```bash
# Create a Pipfile and initialize with python version
pipenv --python 3.6.8 install

# adds requests as dependency package
pipenv install requests

# add a development dependency
pipenv install --dev black pylint pytest

# updates all packages
pipenv update

# update only the requests package
pipenv update requests

# To install all development packages
pipenv install --dev

# Launch pip in the virtual environment.
# pip commands can be used in this shell
pipenv shell

# check vulnerabilities on dependent packages
pipenv check

# Deletes the virtual environment
pipenv --rm
```

* Compatibility with **pip** only environment.

```bash
# below command creates requirements.txt
pipenv lock -r

# once the project has requirements.txt checkin
pip install -r requirements.txt
```

## **Pipfile**

Similar to **Gemfile** in ruby which is managed by bundler. **Pipfile** will be managed by **pipenv**

```Pipfile
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]
black = "*"

[packages]
requests = "*"

[requires]
python_version = "3.7"
```

* **pip** uses **requirements.txt**, while **pipenv** uses **Pipfile**

## Recommendation

* Use **pyenv** to install multiple python versions and set a particular python version for a project.
* Use **pipenv** for managing application dependencies.

---

## References

* [The Python virtual environment with Pyenv & Pipenv](https://dev.to/writingcode/the-python-virtual-environment-with-pyenv-pipenv-3mlo)
* [Pyenv](https://github.com/pyenv/pyenv)
* [Pyenv installer](https://github.com/pyenv/pyenv-installer)
* [Pyenv installation](https://www.tecmint.com/pyenv-install-and-manage-multiple-python-versions-in-linux/)
* [Medium: Pipenv](https://towardsdatascience.com/comparing-python-virtual-environment-tools-9a6543643a44)
* [How to manage multiple Python versions and virtual environments](https://www.freecodecamp.org/news/manage-multiple-python-versions-and-virtual-environments-venv-pyenv-pyvenv-a29fb00c296f/)
* [Python virtual environments dev-dungeon](https://www.devdungeon.com/content/python-virtual-environments-tutorial)

# UV cheatsheet

`uv self update` - updates the uv version

## Manage python versions

```bash
# lists subcommands under python management
uv python --help

# list available python versions
uv python list

# python installation directory. can be customized
uv python dir

# Install a specific version (multiple versions at the same time possible)
uv python install 3.10 3.11

# uninstall version
uv python uninstall 3.10

# to find the installation path of specific python version
uv python find 3.11

# to pin a specific version in the current directory
uv python pin 3.11
```

## Creating Virtual environment

```bash
# if we have pinned the version, we just need
uv venv

# to create venv for a specific python version
uv venv --python 3.11.11
```

## Adhoc Script support

```bash
# running a python script
echo 'print("hello world!")' | uv run -

# multiline script
uv run - <<EOF
print("hello world!")
EOF

# running a script that depends only the standard libs
uv run some_py_script.py

# ignore pyproject.toml deps if the script is not part of the
# project
uv run --no-project example.py

# running scripts with custom packages and version constraints
uv run --with 'pydantic>2.3,<2.5' example.py

# Authoring scripts with python version and dependencies
uv init --script some_py_script.py --python 3.12
uv add --script some_py_script.py 'pydantic>2.5,<2.8' 'requests<3'
uv run some_py_script.py
# When ran with a specific python version, if missing it will be installed.
uv run --python 3.11 some_py_script.py
```

## Project packages management

```bash
uv init my_project

# dev dependency to pyproject.toml
uv add --dev ruff

uv add pydantic==2.8.0

# local editable package installation
uv add --editable "path_to_whl_file"
```

```bash

# Put all the requirements to `requirements.in` and then use the following
# command to generate the `requirements.txt` with all package versions resolved.
# universal option - Perform a universal resolution, attempting to generate a 
# single `requirements.txt` output file that is compatible with all operating 
# systems, architectures, and Python implementations.
uv pip compile requirements.in \
   --universal \
   --output-file requirements.txt


# Install the locked packages from requirements.txt
# sync ensures only these packages are present in the venv
uv pip sync requirements.txt
```

## Pipx Interface

```bash
uv tool list

# install tool using
# install persist the installations
uv tool install ipython@8.14.0

# runs command line tools
uv tool run ipython

# uvx is alias for uv tool run
# with extras and version constaint
# uvx will install and run for that command
uvx --from 'mypy[faster-cache,reports]==1.13.0' mypy --xml-report mypy_report

# when package name and command differs
# the from source can also be a github repo link
uvx --from httpie http

# tool with dependencies and install in isolated environment
# with its own version
uv tool install --isolated --python 3.11 --with cwcwidth bpython

uv tool upgrade ipython
```

## Package build

```bash
uv build

uv build --build-constraint constraints.txt --require-hashes

# to publish to pypi
# Set a PyPI token with --token or UV_PUBLISH_TOKEN, 
# or set a username with --username or UV_PUBLISH_USERNAME 
# and password with --password or UV_PUBLISH_PASSWORD.
# supports publishing to custom index
uv publish --index <name_from_pyproject_uv_index_settings>
```

## References

- [uv docs](https://docs.astral.sh/uv)

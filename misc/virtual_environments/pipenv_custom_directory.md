# Setup virtual environments in custom folders using pipenv

* Install direnv using `sudo apt install direnv` command.
* Add the following line `eval "$(direnv hook bash)"` to `~/.bashrc` file.
* Create a file called `.envrc` in the python project directory and add the `export PIPENV_VENV_IN_PROJECT="enabled"` to the file.
* When we open the folder containing the `.envrc` file the first time, direnv would not load the configuration file. `direnv allow .` needs to be executed to make the direnv run the `.envrc` file next time onwards.

> You may want to see if the direnv project can be useful here. It'll set environment variables for you, automatically, when you enter your project directory, provided you created a `.envrc` file in the project directory and enabled the directory with **direnv**. You then can add any such export commands to that file. [StackOverflow answer](https://stackoverflow.com/questions/52540121/make-pipenv-create-the-virtualenv-in-the-same-folder)

---

## References

* [Pipenv virtual environment custom directory](https://stackoverflow.com/questions/52540121/make-pipenv-create-the-virtualenv-in-the-same-folder)
* [Setting up direnv](https://direnv.net/docs/installation.html)

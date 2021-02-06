#!/bin/bash
FILE=$1

echo "Running isort"
pipenv run isort "$FILE"

echo "Running autoflake"
pipenv run autoflake -i --remove-all-unused-imports "$FILE"

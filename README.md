# Lab: 31 - Django REST Framework

## Tools Used

VS Code

Python

Django

flake8

black

djangorestframework

## Feature Tasks and Requirements

- [x] Rebuild a custom version of Blog API demo project from scratch.
- [x] Replace Blog and Post with your own application and model.
- [x] Your model must have at least as many fields as demo’s model.
- [x] Your model must have one field that is a foreign key to user.
      NOTE: You are not required to build any templates for this lab.

## Features - Docker

- [x] NOTE Refer to the class demo for built out Dockerfile and docker-compose.yml examples.
- [x] Update Dockerfile and docker-compose.yml if needed.

## Implementation Notes

- [x] You’ll need to run a command to convert pyproject.toml dependencies to requirements.txt
      `poetry export -f requirements.txt -o requirements.txt`
- [x] If you get an allowed host error examine the bug details and update code as needed.
- [x] When Docker installed and docker files are ready to go then run… `$ docker-compose up`

## Configuration

- [x] Use poetry to initialize drf-api project.

```
$ mkdir drf-api

$ cd drf-api

$ poetry init -n

$ poetry shell
```

Then continue to build the Django project.

Use the drf-api folder as the root of your project’s git repository.

## Developer

Faisal Kushha

## Pull requests

https://github.com/Faisal-Kushha/laptop-api/pull/1

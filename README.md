Django Fullstack Template
=========================

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)-Template for a fullstack [Django](https://www.djangoproject.com/) project. 

## Requirements

- Python >= 3.11
- [Poetry](https://python-poetry.org/) >= 1.5.1

## Usage

### Cookiecutter

First create a virtual env using poetry and install the required packages with `poetry install` in the root folder (where this readme file is placed). Then run `poetry run cookiecutter .` to create a new project from this template. You will be asked to enter some values for the project.

### Backstage



## Included features

- [Poetry](https://python-poetry.org/) for python dependency management
- Jetbrains [PyCharm](https://www.jetbrains.com/pycharm/) as IDE
- [Django](https://www.djangoproject.com/) as fullstack web framework with following additional libraries:
  - [Django admin site](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/): an automatic admin interface for your models
  - [django-import-export](https://django-import-export.readthedocs.io/): importing and exporting data (with admin integration!)
  - [whitenoise](https://whitenoise.readthedocs.io/): serving static files directly from within the WSGI application


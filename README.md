Django Fullstack Template
=========================

This is a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)-Template for a fullstack [Django](https://www.djangoproject.com/) project. 

## Requirements

- Python >= 3.11
- [Poetry](https://python-poetry.org/) >= 1.5.1

## Getting started

### Cookiecutter

First create a virtual env using poetry and install the required packages with `poetry install` in the root folder (where this readme file is placed). Then run `poetry run cookiecutter .` to create a new project from this template. You will be asked to enter some values for the project. After that you have a new django project in the folder you specified.

### Backstage

TBD

## Included features (deviant from the default django "startproject" output)

- [Poetry](https://python-poetry.org/) for python dependency management
- Jetbrains [PyCharm](https://www.jetbrains.com/pycharm/) as IDE
- [Django](https://www.djangoproject.com/) as fullstack web framework:
  - Additional libraries/apps:
    - [Django admin site](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/): an automatic admin interface for your models
    - [django-import-export](https://django-import-export.readthedocs.io/): importing and exporting data (with admin integration!)
    - [whitenoise](https://whitenoise.readthedocs.io/): serving static files directly from within the WSGI application
    - [django-environ](https://django-environ.readthedocs.io/): set all django settings through environment variables (see [12factor](https://12factor.net/config))
    - [python-dotenv](https://pypi.org/project/python-dotenv/): easy loading of environment variables from a `.env` file
  - Settings:
    - Using [ManifestStaticFilesStorage](https://docs.djangoproject.com/en/4.2/ref/contrib/staticfiles/#manifeststaticfilesstorage) as default staticfiles storage. This will automatically prepend a hash to the filename of each static file and update the references in the templates. This is useful for cache busting.
    - In debug-mode the [console.EmailBackend](https://docs.djangoproject.com/en/4.2/topics/email/#console-backend) is used as default email backend. This will print all emails to the console instead of sending them.
    - Default language and timezone are set to german and europe/berlin respectively.

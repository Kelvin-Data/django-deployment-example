#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# django admin startproject ProTwo
# cd ProTwo
# Python manage.py startapp appTwo

# create new template folder
# create appTwo folder under the templates
# create 2 htmls index.html & users.html under the appTwo folder

# python manage.py migrate
# python manage.py makemigrations appTwo
# python manage.py migrate

# python manage.py runserver

# python manage.py createsuperuser
# username : Kelvin
# Email : training@gmail.com
# Password : simple123

# python populate_users.py
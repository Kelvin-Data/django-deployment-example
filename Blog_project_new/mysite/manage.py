#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
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

# python manage.py migrate
# python manage.py makemigrations blog
# python manage.py migrate
# python manage.py createsuperuser

# Username : lbh
# Email : simple123@yahoo.com
# Password : simple123

# python manage.py runservercd..

# http://127.0.0.1:8000/accounts/user
# http://127.0.0.1:8000/post/new/
# http://127.0.0.1:8000/drafts/

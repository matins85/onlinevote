#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv


def main():
    """Run administrative tasks."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    try:
        dotenv.read_dotenv(base_dir, '.env')
    except IsADirectoryError:
        dotenv.read_dotenv()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onlinevote.settings')
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

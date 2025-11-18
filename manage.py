#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# Force thin mode; ignore any local Oracle client env
for v in ("ORACLE_HOME","DYLD_LIBRARY_PATH","LD_LIBRARY_PATH"):
    os.environ.pop(v, None)



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cps510_gui.settings')
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

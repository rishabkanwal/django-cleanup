#!/usr/bin/env python
import sys
from django.conf import settings

settings.configure(
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        },
    },
    INSTALLED_APPS = (
        'django_cleanup.testapp',
        'django_cleanup',
    ),
    MIDDLEWARE_CLASSES = [],
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv[:1] + ['test'] + sys.argv[1:])
#!/usr/bin/env python
from os.path import dirname, join, realpath
import sys

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'autocomplete_light',
            'django.contrib.admin',
            'pagination',
            'slug_helpers',
            'file_archive',
            'info',
        ),
        SITE_ID=1,
        SECRET_KEY='this-is-just-for-tests-so-not-that-secret',
        ROOT_URLCONF='info.urls',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    realpath(join(dirname(__file__), 'example_templates'))
                ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.contrib.auth.context_processors.auth',
                    ],
                },
            },
        ],
        MARKITUP_FILTER=(
            'markdown.markdown',
            {'safe_mode': True, 'extensions':['tables']}
        ),
        INFO_PAGES_ALLOW_RAW_HTML=False,
        INFO_POSTS_PER_LIST_PAGE=10,
        MEDIA_URL='/media_root/',
    )

def runtests():
    django.setup()
    test_runner = DiscoverRunner(verbosity=1)
    failures = test_runner.run_tests(['info'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()

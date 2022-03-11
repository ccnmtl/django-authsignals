""" run tests for django-authsignasl

$ virtualenv ve
$ ./ve/bin/pip install Django==1.8
$ ./ve/bin/pip install -r test_reqs.txt
$ ./ve/bin/python runtests.py
"""


import django
from django.conf import settings
from django.core.management import call_command


def main():
    # Dynamically configure the Django settings with the minimum necessary to
    # get Django running tests
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'testapp',
            'authsignals',
        ),
        TEST_RUNNER='django.test.runner.DiscoverRunner',
        AUTHSIGNALS_SUPERUSERS=[
            'testadmin1',
            'testadmin2',
        ],

        COVERAGE_EXCLUDES_FOLDERS=['migrations'],
        ROOT_URLCONF='testapp.urls',
        SECRET_KEY='dummy',

        PROJECT_APPS=[
            'authsignals',
        ],
        # Django replaces this, but it still wants it. *shrugs*
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
                'HOST': '',
                'PORT': '',
                'USER': '',
                'PASSWORD': '',
            }
        },
    )

    django.setup()

    call_command('check')
    # Fire off the tests
    call_command('test')

if __name__ == '__main__':
    main()

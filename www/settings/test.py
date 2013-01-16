# settings that apply in dev

from ..settings import *
from www import version

DEBUG = False
CELERY_ALWAYS_EAGER = True

# if you're using django nose, uncomment the following
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#if 'django_nose' not in INSTALLED_APPS:
#    INSTALLED_APPS += ('django_nose',)
#NOSE_ARGS = ('--cover-erase', '--with-xcoverage', '--cover-branches',
#             '--cover-package=www', '--cover-html', '--with-xunit', '--stop')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite3_tests.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'madefire-web',
        'KEY_PREFIX': str(random()),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%SZ',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'filename': 'django.log',
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ('console', 'file'),
    },
    'loggers': {
        'boto': {
            'level': 'INFO',
        },
        'django.db.backends': {
            # comment out to see db queries
            'level': 'DEBUG',
        },
    },
}

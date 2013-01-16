# settings that apply in dev

from ..settings import *
from www import version

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djconf',
        'USER': DB_USERNAME,
        'PASSWORD': DB_PASSWORD,
        'HOST': DB_HOSTNAME,
        'PORT': '3306',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',
        # important to put the version here so that you won't use objects put
        # in to the cache by previous versions of your app (which could now be
        # wrong.)
        'KEY_PREFIX': version,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LOGGING = {
    'version': 1,
    'formatters': {
        'syslog': {
            'format': 'web: [%(process)s] %(levelname)s %(name)s %(message)s',
        },
    },
    'handlers': {
        'syslog':{
            'class':'logging.handlers.SysLogHandler',
            'level':'INFO',
            'formatter': 'syslog',
            'address': '/dev/log',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ('syslog',),
    },
    'loggers': {
        'celery': {
            'level': 'INFO',
        },
        'multiprocessing': {
            'level': 'INFO',
        },
        'ssh': {
            'level': 'WARN',
        }
    }
}

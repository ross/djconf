# settings that apply in dev

from ..settings import *
from www import version

DEBUG = True
CELERY_ALWAYS_EAGER = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite3.db',
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
        # important to put the version here so that you won't use objects put
        # in to the cache by previous versions of your app (which could now be
        # wrong.)
        'KEY_PREFIX': version,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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
            'level': 'DEBUG',
            'formatter': 'simple',
        },
        'file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': 'django.log',
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ('console', 'file'),
    },
    'loggers': {
        'boto': {
            'level': 'INFO',
        },
        'celery': {
            'level': 'INFO',
        },
        'django.db.backends': {
            # comment out to see db queries
            'level': 'INFO',
        },
        'multiprocessing': {
            'level': 'INFO',
        },
        'ssh': {
            'level': 'WARN',
        }
    },
}

# django debug toolbar
MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + \
        MIDDLEWARE_CLASSES
INSTALLED_APPS += ('debug_toolbar',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}
DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.cache.CacheDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
    'django_statsd.panel.StatsdPanel'
)

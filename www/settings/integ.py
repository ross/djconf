# settings that apply in dev

from ..settings import *
from www import version

DEBUG = True
ASSETS_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'web',
        'USER': 'web',
        'PASSWORD': 'b3ef779462c04689b85c68e3da5fbce0',
        'HOST': 'localhost',
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
        'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%SZ',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': 'DEBUG',
            'formatter': 'simple',
            'filename': 'django.log',
        }
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ('file',),
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
        },
        'statsd': {
            'level': 'INFO',
            # single out stats in to their own file
            'handlers': ('stats',),
            'propagate': False
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
)

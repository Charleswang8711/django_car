from .base import *

WEBPACK_LOADER = {
    'DEFAULT': {
            'BUNDLE_DIR_NAME': 'bundles/',
            'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.prod.json'),
        }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'urver_db',
        'USER': 'urver',
        'PASSWORD': os.environ.get('DB_PASSWORD', 'urver_db_password'),
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

DEBUG = True if os.environ.get('DEBUG') == '1' else False
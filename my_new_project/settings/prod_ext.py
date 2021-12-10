from .prod import *

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER' : 'armis',
        'PASSWORD' : 'qwerty',
        'HOST' : '127.0.0.1',
        'PORT' : '54323',
    }
}
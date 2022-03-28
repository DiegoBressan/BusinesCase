from logging import root

import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()

SECRET_KEY= env(261998)

POSTGRESQL_NAME='BusinesCaseDataBase'
POSTGRESQL_USER='root'
POSTGRESQL_PASS=261998
POSTGRESQL_HOST='127.0.0.1'
POSTGRESQL_PORT=5432
DEBUG= env('DEBUG')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRESQL_NAME'),
        'USER': env('POSTGRESQL_USER'),
        'PASSWORD': env('POSTGRESQL_PASS'),
        'HOST': env('POSTGRESQL_HOST'),
        'PORT': env('POSTGRESQL_PORT'),
    }
}
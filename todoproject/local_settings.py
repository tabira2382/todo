import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'n84qw#7^azwtc(c&isq21k28nxr&+zzufmi7q(pw72v@7m8%y9'


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.path.join(BASE_DIR,'db.sqlite3')
    }
}
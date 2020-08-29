from .base import *
# SECURITY WARNING: don't run with debug turned on in production!

#Para local
DEBUG = True
#Docker
"""DEBUG = False"""

#Local
ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


#LOCAL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


#EN LOCAL
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


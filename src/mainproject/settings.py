
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nmlmxv#v&1)htm!rq$5n&et%)qdrf-n)i*ygr4gqaf^pu-4^ea'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_tables2',
    # our apps
    'personnel',
    'operationCommerciale',
    'formation',
    'zone',
    'surveillance',
    'releveSanitaire',
    'api_direction_generale',
    'Ruby',
    # our externe DB
    'db_chili',
    'db_danemark',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mainproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mainproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'de4d2pmm5uu33p',
        'USER': 'cgvewbkdwlhmfd',
        'PASSWORD': 'd6c9fd76eb862219c0341936a37c93a9b5b8add9b8a569bc3e53d5dc1f57ff08',
        'HOST': 'ec2-79-125-123-149.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    },
    'site_chili': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd803n5ifs6ff1p',
        'USER': 'kkcpvqllcdqywo',
        'PASSWORD': 'a22513d20ce317b3d3d674b9a8392152125f7acc0fe114cab2ff7bbaad3188d0',
        'HOST': 'ec2-54-217-195-234.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    },
    'site_danemark': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_81c277e85c2e8d4',
        'USER': 'b2075f4f77d3a4',
        'PASSWORD': '83f7ec6d',
        'HOST': 'eu-cdbr-west-02.cleardb.net',
        'PORT': '3306',
    },

}
# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

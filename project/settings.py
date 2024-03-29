"""
Django settings for pages project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
import env_file

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'https://www.youtube.com/channel/UCTZUTvv_1Onm-f-533Hyurw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = "build" not in sys.argv

ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'bakery',
    'corsheaders',
    'emoji',
    'webpack_loader',

    "taggit",
    "django_github_user",

    'apps.gists',
    'apps.repos',
    'apps.starred_gists',
    'apps.starred_repos',
    "project",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SECURITY_MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
]

# This is required to go first! See: https://github.com/ottoyiu/django-cors-headers#setup
CORS_MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

DJANGO_MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE = SECURITY_MIDDLEWARE + CORS_MIDDLEWARE + DJANGO_MIDDLEWARE

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
env_file.load(path)

SECRET_KEY = "https://www.youtube.com/channel/UCTZUTvv_1Onm-f-533Hyurw"
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER', os.getenv('USER', 'postgres')),
        'PASSWORD': os.getenv('DB_PASS', ''),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

WSGI_APPLICATION = 'project.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

GITHUB_USERNAME = os.popen("git config user.name").read().strip()
GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]

# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
"""
AWS_STATIC_BUCKET_NAME = "web-%s-github-io-static" % USERNAME
AWS_STATIC_DOMAIN = '%s.s3.amazonaws.com' % AWS_STATIC_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_STATIC_DOMAIN
"""

WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.dev.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}
if not DEBUG:
    WEBPACK_LOADER['DEFAULT'].update({
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.production.json')
    })

"""
CORS_ORIGIN_ALLOW_ALL = True
has been blocked by CORS policy: The value of the 'Access-Control-Allow-Origin' header in the response must not be the wildcard '*' when the request's credentials mode is 'include'. The credentials mode of requests initiated by the XMLHttpRequest is controlled by the withCredentials attribute
"""

CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'google.com',
    'hostname.example.com',
    'localhost:8000',
    '127.0.0.1:8000'
)

BAKERY_VIEWS = (
    'apps.gists.views.StaticView',
    'apps.repos.views.StaticView',
    'apps.starred_gists.views.StaticView',
    'apps.starred_repos.views.StaticView',
)

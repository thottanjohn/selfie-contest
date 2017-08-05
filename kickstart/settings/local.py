
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f*r+hbg=mm)83k*z@uc9)0#vx-q&ubvtp1*mn18kw2--30-r(k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

		
# Application definition

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'registration' ,
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #third party apps
    'crispy_forms',
    'social_django', 
    'selfiecontest',
    ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'kickstart.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect',
               ],
        },
    },
]
AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'kickstart.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
        'USER': 'thottanjohn',
        'PASSWORD': 'family',
    }
}



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
SOCIAL_AUTH_GITHUB_KEY= 'a53b650e72ed5c7f110f'
SOCIAL_AUTH_GITHUB_SECRET='0c05b9cbb5e7fc8e2402b83406286658b40d9608'



STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static_in_pro","our_static"),
)



MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_in_env","media_root")
MEDIA_URL='/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap3' 

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thottanjohn@gmail.com'
EMAIL_HOST_PASSWORD = 'johntony'
EMAIL_PORT = 587

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN =True
SITE_ID=1
LOGIN_REDIRECT_URL ="/"


SOCIAL_AUTH_TWITTER_KEY = '9ao6C646gtHbjTCONTMTDorga'

SOCIAL_AUTH_TWITTER_SECRET = 'lYtoolx8WVGS75YqLzxxBCJPzUPo9QcEtpMketOoc7PXYEqCbL'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '722048099772-lk76rle6r92cas9o7ck43c03vsdlghlq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Qpr8qAT71eS6Ydxningweqih'
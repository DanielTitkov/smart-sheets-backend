import os
from configurations import Configuration, values
import sys 

# adding app folder to python path
# otherwise gunicorn would not be able to find app.accounts etc
# and changing import paths manually is not that entertaining
sys.path = [os.path.dirname(os.path.dirname(os.path.abspath(__file__)))] + sys.path 

class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = values.Value("secret_key")
    VK_SECRET_KEY = values.Value("vk_key")
    ALLOWED_HOSTS = []
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        # third-party
        'corsheaders',
        'rest_framework',
        # internal
        'accounts',
        'sheets',
    ]
    MIDDLEWARE = [
        'corsheaders.middleware.CorsMiddleware', # cors
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    ROOT_URLCONF = 'app.urls'
    AUTHENTICATION_BACKENDS = [
        'accounts.backends.VkBackend',
        'django.contrib.auth.backends.ModelBackend',
    ]
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
    WSGI_APPLICATION = 'app.wsgi.application'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': values.Value("database_name", environ_name="DATABASE_NAME"),
            'USER' : values.Value("database_user", environ_name="DATABASE_USER"),
            'PASSWORD' : values.Value("database_password", environ_name="DATABASE_PASSWORD"),
            'HOST' : values.Value("localhost", environ_name="DATABASE_HOST"),
            'PORT' : values.Value("5432", environ_name="DATABASE_PORT"),
        }
    }
    AUTH_PASSWORD_VALIDATORS = [
        {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
        {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
        {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
        {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    ]
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'accounts.backends.VkBackendREST',
        ],
        'DEFAULT_RENDERER_CLASSES': (
            'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
            'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'djangorestframework_camel_case.parser.CamelCaseFormParser',
            'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
            'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        ),
    }
    CORS_ORIGIN_ALLOW_ALL = True
    # CORS_ORIGIN_WHITELIST = [
    #     'http://localhost:10888'
    # ]
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    STATIC_URL = '/static/'
    STATIC_ROOT = 'static'
    DEFAULT_USER_PASSWORD_LENGTH = 16



class Dev(Base):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG



class Local(Dev):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '127.0.0.1',
            'PORT': values.Value("5432", environ_name="DATABASE_PORT"),
            # 'USER': 'gapp',
            # 'PASSWORD': '123123',
            # 'NAME': 'gapp',
        }
    }



class Deploy(Base):
    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    ROOT_URLCONF = "app.app.urls"
    ALLOWED_HOSTS = [
        'smart-sheets-backend.appspot.com',
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': '/cloudsql/smart-sheets-backend:europe-west3:postgres1',
            # 'USER': 'gapp',
            # 'PASSWORD': '123123',
            # 'NAME': 'gapp',
        }
    }



class Prod(Deploy):
    DEBUG = False
    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
        'DEFAULT_AUTHENTICATION_CLASSES': [
            'accounts.backends.VkBackendREST',
            # 'rest_framework.authentication.BasicAuthentication',
            # 'rest_framework.authentication.SessionAuthentication',
        ],
        'DEFAULT_RENDERER_CLASSES': (
            'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
            'djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer',
        ),
        'DEFAULT_PARSER_CLASSES': (
            'djangorestframework_camel_case.parser.CamelCaseFormParser',
            'djangorestframework_camel_case.parser.CamelCaseMultiPartParser',
            'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        ),
    }
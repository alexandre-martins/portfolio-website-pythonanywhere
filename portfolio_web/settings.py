import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n%-a$2h&x18dmo2*^+%bb*i2m^t(dk$kr15!6#cv8(mec!6x5@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['alexandremartins.pythonanywhere.com/']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'articles',
    'ckeditor',
    'ckeditor_uploader',
]

CKEDITOR_UPLOAD_PATH = 'post-uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'allowedContent': True,
        'autoParagraph': False,
        'removePlugins': 'stylesheetparser,about,showblocks,language,form,flash,iframe',
        'height': 700,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ["Format", "Font", "FontSize", "Bold", "Italic", "Underline", "Strike", "SpellChecker"],
            ['NumberedList', 'BulletedList', "Indent", "Outdent"],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ["Image", "Table", "Link", "Unlink", "Anchor", "SectionLink"],
            ["Subscript", "Superscript"],
            ['Undo', 'Redo'], 
            ['CodeSnippet'],
            ['Blockquote'],
            ['EqnEditor'],
            ["Source"],
            ["Maximize"]
        ],
        'extraPlugins': ['codesnippet', 'blockquote', 'eqneditor']
    },
    'overview': {
        'height': 300,
        'toolbar': 'Overview',
        'toolbar_Overview': [
            ["Format", "Bold", "Italic", "Underline", "Strike", "SpellChecker"]
        ]
    }
}

CKEDITOR_SETTINGS = {
    'format_tags': 'p;h1;h2;h3;h4;h5;h6;pre;address;div;blockquote'
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['portfolio-website-pythonanywhere/templates'],
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

WSGI_APPLICATION = 'portfolio_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = '/home/alexandremartins/portfolio-website-pythonanywhere/static'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

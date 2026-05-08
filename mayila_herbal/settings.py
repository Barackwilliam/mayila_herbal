from pathlib import Path
from decouple import config
# Deployed in render using this email account botikawilly@gmail.com

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-mayila-herbal-change-in-production')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tinymce',  # ongeza hapa
    'core',
    'products',
    'videos',
]


# TinyMCE Configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 400,
    'menubar': 'file edit view insert format tools',
    'plugins': [
        'advlist', 'autolink', 'lists', 'link', 'charmap', 'preview',
        'searchreplace', 'visualblocks', 'code', 'fullscreen',
        'insertdatetime', 'table', 'paste', 'wordcount', 'help',
    ],
    'toolbar': (
        'undo redo | formatselect | bold italic underline | '
        'alignleft aligncenter alignright | '
        'bullist numlist | removeformat | '
        'pastetext | code fullscreen | help'
    ),

    # ✅ Hii ndiyo muhimu — inasafisha paste kutoka Word/PDF automatically
    'paste_as_text': False,
    'paste_word_valid_elements': 'p,b,strong,i,em,h1,h2,h3,ul,ol,li,br',
    'paste_retain_style_properties': 'none',
    'paste_remove_styles_if_hints': True,
    'paste_strip_class_attributes': 'all',

    'content_css': False,
    'skin': 'oxide',
    'content_style': '''
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 14px;
            line-height: 1.6;
            color: #333;
            padding: 12px;
        }
        p { margin: 0 0 10px 0; }
        ul, ol { padding-left: 20px; margin: 0 0 10px 0; }
    ''',
}

# Kwa benefits field — editor ndogo bila formatting nyingi
TINYMCE_BENEFITS_CONFIG = {
    'height': 220,
    'menubar': False,
    'plugins': ['lists', 'paste'],
    'toolbar': 'bullist numlist | removeformat | pastetext',
    'paste_as_text': True,  # Benefits: paste as plain text tu
    'forced_root_block': 'p',
    'content_style': '''
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            font-size: 14px;
            line-height: 1.8;
            color: #333;
            padding: 12px;
        }
    ''',
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


ROOT_URLCONF = 'mayila_herbal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'mayila_herbal.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres.aenenssvaruafzprapsp',
        'PASSWORD': 'NyumbaChap@123',
        'HOST': 'aws-0-eu-west-1.pooler.supabase.com',
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {
            'sslmode': config('DB_SSLMODE', default='require'),
        },
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

UPLOADCARE = {
    'pub_key': config('UPLOADCARE_PUBLIC_KEY', default='4c3ba9de492e0e0eaddc'),
    'secret': config('UPLOADCARE_SECRET_KEY', default='28410d13b3cb1098451e'),
}

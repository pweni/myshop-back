from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kqpn@p8&y2m8*y#pqix0=^fda=%qwj$)1&x7lv2m@7#@*&*2$o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.basic',
    'apps.goods',
    'apps.member',
    'apps.order',
    'apps.users',
    'ckeditor',
    'ckeditor_uploader',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'app6.middle.mymiddle.AuthMiddleware1',
    #'app6.middle.mymiddle.AuthMiddleware2'
]

ROOT_URLCONF = 'myshop.urls'

AUTH_USER_MODEL="users.MyUser"
LOGIN_URL = '/diy_login/'  #这个路径需要根据你网站的实际登陆地址来设置
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'shop',
        'USER': 'root',
        'PASSWORD': '123456',#Aa_123456
        'HOST': '127.0.0.1',#42.192.201.44
        'PORT': '3306',
        #取消外键约束，否则多对多模型迁移报django.db.utils.IntegrityError: (1215, 'Cannot add foreign key constraint')
            'OPTIONS': {
            "init_command": "SET foreign_key_checks = 0;",
        }
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
STATIC_ROOT = os.path.join(BASE_DIR, '/static')

MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5,
}

CKEDITOR_UPLOAD_PATH='upload/'
CKEDITOR_IMAGE_BACKEND='pillow'
# 富文本编辑器ckeditor配置
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
            ['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
            ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll', 'RemoveFormat'],
            ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
            ['Blockquote', 'CodeSnippet'],
        ),
        'width': 'auto',
    },
}

""" # 设置redis存储session信息
SESSION_ENGINE = 'redis_sessions.session'
# redis服务的ip地址
SESSION_REDIS_HOST = '192.168.77.101'
# redis服务的端口号
SESSION_REDIS_PORT = 6379
# redis中的哪一个数据库
SESSION_REDIS_DB = 2
# 链接redis的密码，没有写空
SESSION_REDIS_PASSWORD = '123456'
# 指定session信息的前缀
SESSION_REDIS_PREFIX = 'session' """

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://192.168.77.101:6379",
        "OPTIONS": {
            "CLIENT_CLASS":"django_redis.client.DefaultClient",
            "PASSWORD":"123456",
        }
    }
}

# session的存储配置
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# 设置session失效时间,单位为秒
SESSION_COOKIE_AGE = 60*5

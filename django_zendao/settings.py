import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

SECRET_KEY = 'u+o5dz4t$-yk)kt)iznr#tvahmioqd@p79p65&2=706@d5hah&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

INSTALLED_APPS = [
    'simpleui',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',
    'corsheaders',
    'import_export',
    'taggit',
    'ckeditor',
    'ckeditor_uploader',
    # 'DjangoUeditor',

    'mdoc',
    'mproduct',
    'mproject',
    'msystem',
    'mtest',
    'muser'
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

ROOT_URLCONF = 'django_zendao.urls'

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

WSGI_APPLICATION = 'django_zendao.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db2.sqlite3'),
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_FORMAT = 'Y-m-d'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "uploads"),
)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False  # 是否使用TLS安全传输协议
EMAIL_USE_SSL = True  # 是否使用SSL加密，qq企业邮箱要求使用
EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

# 跨域 -----------------------------------------------
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'http://127.0.0.1:8080',
    'http://localhost:9292',  # 凡是出现在白名单中的域名，都可以访问后端接口
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# djangorestframework配置 -----------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly', ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.AutoSchema",
}


# django-simpleui配置 -----------------------------------------------
SIMPLEUI_HOME_INFO = False
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_ANALYSIS = False

SIMPLEUI_CONFIG = {
    'system_keep': True,
    'menu_display': ['产品管理', '项目管理', '测试管理', '文档管理','认证和授权'],
}


SIMPLEUI_ICON = {
    '产品管理': 'fas fa-link', '产品': 'fas fa-server', '产品版本': 'fas fa-code-branch', '产品需求': 'fas fa-link',
    '项目管理': 'fas fa-cube', '项目': 'fas fa-suitcase', '任务': 'fas fa-list',
    '测试管理': 'fas fa-flask', '测试计划': 'fas fa-calendar','测试用例': 'fas fa-vial','缺陷': 'fas fa-bug',
    '文档管理': 'fas fa-suitcase', '文档库': 'fas fa-book', '文档': 'fas fa-file-alt'
}


# django-ckeditor
CKEDITOR_UPLOAD_PATH = '/static/media'

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
    # 'simpleui',

    # 'grappelli',
    "admin_interface",
    "colorfield",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # for admin
    'nested_admin',
    'import_export',
    'taggit',
    'tinymce',
    'notifications',
    'crispy_forms',
    'treenode',
    'extra_settings',
    # 'loginas',
    # 'django_comments',
    # 'attachments',

    # 'admin_reorder',

    # for api
    'rest_framework',
    'django_filters',
    'corsheaders',

    # out apps
    'mproduct',
    'mproject',
    'mdoc',
    'mtest',
    'muser',
    'msystem',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # added
    # 'admin_reorder.middleware.ModelAdminReorder',
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
                # 'loginas.context_processors.impersonated_session_status',
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
# LANGUAGE_CODE = 'ru'

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

# # django-simpleui配置 -----------------------------------------------
# SIMPLEUI_HOME_INFO = False
# SIMPLEUI_STATIC_OFFLINE = True
# SIMPLEUI_ANALYSIS = False
#
# SIMPLEUI_CONFIG = {
#     'system_keep': True,
#     'menu_display': ['产品管理', '项目管理', '测试管理', '文档管理','认证和授权'],
# }
#
#
# SIMPLEUI_ICON = {
#     '产品管理': 'fas fa-link', '产品': 'fas fa-server', '产品版本': 'fas fa-code-branch', '产品需求': 'fas fa-link',
#     '项目管理': 'fas fa-cube', '项目': 'fas fa-suitcase', '任务': 'fas fa-list',
#     '测试管理': 'fas fa-flask', '测试计划': 'fas fa-calendar','测试用例': 'fas fa-vial','缺陷': 'fas fa-bug',
#     '文档管理': 'fas fa-suitcase', '文档库': 'fas fa-book', '文档': 'fas fa-file-alt'
# }
#
#
# # django-ckeditor
# CKEDITOR_UPLOAD_PATH = '/static/media'


# tinymce配置
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 300,
    "menubar": False,
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
               "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
               "code,help,wordcount",
    "toolbar": "undo redo | formatselect | "
               "bold italic backcolor | alignleft aligncenter "
               "alignright alignjustify | bullist numlist outdent indent | "
               "removeformat | help",
    "language": "zh_CN"
}

APP_LIST = {
    'mproduct': {'order': 1, 'models': ['Product', 'ProductVersion', 'ProductPlan']},
    'mproject': {'order': 2, 'models': ['Project', 'Requirement', 'Task']},
    'mtest': {'order': 3, 'models': ['Bug', 'TestCase', 'TestPlan']},
    'mdoc': {'order': 4, 'models': ['DocLibrary', 'Doc']},
    'auth': {'order': 5},
    'admin': {'order': 6}
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "...",
    },
    "treenode": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
}

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]


# AUTH_PROFILE_MODULE = 'muser.UserProfile'
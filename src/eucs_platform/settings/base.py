"""
Django settings for eucs_platform project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.urls import reverse_lazy
from machina import MACHINA_MAIN_TEMPLATE_DIR, MACHINA_MAIN_STATIC_DIR
from pathlib import Path
import os
import platform
from django.contrib import messages
# Use 12factor inspired environment variables or from a file
import environ

# Build paths inside the project like this: BASE_DIR / "directory"
BASE_DIR = Path(__file__).resolve().parent.parent.parent
STATIC_ROOT = "/home/ubuntu/eu-citizen.science_07_08/static"
THEMEDIRSTATIC = str(BASE_DIR / "eucitizensciencetheme" / "static")
STATICFILES_DIRS = [str(BASE_DIR / "static"), MACHINA_MAIN_STATIC_DIR, THEMEDIRSTATIC]

# settings.py
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATIC_VERSION = '1.5'
THEME = 'eucitizenscience'
#THEME = 'portugal'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = str(BASE_DIR / "media")
MEDIA_URL = "/media/"
THUMBNAIL_DEBUG = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    },
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Tell select2 which cache configuration to use:
SELECT2_CACHE_BACKEND = "select2"

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(BASE_DIR / "templates"),
            MACHINA_MAIN_TEMPLATE_DIR,
            # insert more TEMPLATE_DIRS here
            str(BASE_DIR / "themes" / THEME / "templates")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.request',
                # Machina
                'machina.core.context_processors.metadata',
                # Wwn
                'eucs_platform.context_processors.global_settings',
                # To manage static versions
                'eucs_platform.context_processors.static_version',
                # To manage the theme
                'eucs_platform.context_processors.theme',
            ]
        },
    }
]

env = environ.Env()

# Create a local.env file in the settings directory
# But ideally this env file should be outside the git repo
env_file = Path(__file__).resolve().parent / "local.env"
if env_file.exists():
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env("SECRET_KEY", default="CHANGEME!!!")
PLATFORM_NAME = env("PLATFORM_NAME", default="EuCitizenScience")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    "modeltranslation",
    "eucitizensciencetheme",
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "authtools",
    "crispy_forms",
    "easy_thumbnails",
    "profiles",
    "accounts",
    "projects",
    "resources",
    "digest",
    "platforms",
    "django_select2",
    "blog",
    "pages",
    "django_summernote",
    "leaflet",
    "django_countries",
    "authors",
    "contact",
    "reviews",
    #'ecsa_integration',
    'django.contrib.sites',
    'cookielaw',
    'events',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
    'rest_framework_swagger',
    'oidc_provider',
    'drf_yasg',
    'django_recaptcha',
    'active_link',
    'oauth2_provider',
    'django.contrib.gis',

    # Machina dependencies:
    'mptt',
    'haystack',
    'widget_tweaks',

    # Machina apps:
    'machina',
    'machina.apps.forum',
    'machina.apps.forum_conversation',
    'machina.apps.forum_conversation.forum_attachments',
    'machina.apps.forum_conversation.forum_polls',
    'machina.apps.forum_feeds',
    'machina.apps.forum_moderation',
    'machina.apps.forum_search',
    'machina.apps.forum_tracking',
    'machina.apps.forum_member',
    'machina.apps.forum_permission',

    'organisations',
    'django_cron',
    'django_crontab',
    'ckeditor',
    'ckeditor_uploader',
    'django_ckeditor_5',
    'fontawesomefree',


)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    'eucitizensciencetheme.middleware.TopBarMiddleware',
    'eucitizensciencetheme.middleware.FooterMiddleware',
    # Machina
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # TopBar
    
]

ROOT_URLCONF = "eucs_platform.urls"
WSGI_APPLICATION = "eucs_platform.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env("DATABASE_NAME", default="eucs_platform"),
        'USER': env("DATABASE_USER", default="eucs_platform"),
        'PASSWORD': env("DATABASE_PASSWORD", default="eucs_platform"),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


LANGUAGE_CODE = "en"

TRANSLATED_LANGUAGES = (
    ('nl', 'Dutch'),
    ('en', 'English'),
    ('et', 'Estonian'),
    ('fr', 'Français'),
    ('de', 'German'),
    ('el', 'Greek'),
    ('hu', 'Hungarian'),
    ('it', 'Italian'),
    ('lt', 'Lituanian'),
    ('pt', 'Portuguese'),
    ('es', 'Spanish'),
    ('sv', 'Swedish'),
)
LANGUAGE_CODES = [
    'fr',
    'en',
    'ar',
    'am',
    'bg',
    'bn',
    'ca',
    'cs',
    'da',
    'de',
    'el',
    'es',
    'et',
    'fa',
    'fi',
    'fil',
    'gu',
    'he',
    'hi',
    'hr',
    'hu',
    'id',
    'ga',
    'it',
    'ja',
    'kn',
    'ko',
    'lt',
    'lv',
    'ml',
    'mr',
    'ms',
    'mt',
    'nl',
    'no',
    'pl',
    'pt',
    'ro',
    'ru',
    'sk',
    'sl',
    'sr',
    'sv',
    'sw',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'vi',
    'zh_CN'
]

MODELTRANSLATION_LANGUAGES = (
    'en', 'es', 'pt', 'nl', 'et', 'fr', 'de', 'el', 'hu', 'it', 'lt', 'sv')
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = "/static/"

ALLOWED_HOSTS = ["*"]

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = "bootstrap3"


MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
# Authentication Settings
AUTH_USER_MODEL = "authtools.User"
LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGIN_URL = reverse_lazy("accounts:login")


THUMBNAIL_EXTENSION = "png"  # Or any extn for your thumbnails

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (40.0, -3.0),
    'DEFAULT_ZOOM': 2,
    'MIN_ZOOM': 2,
    'RESET_VIEW': False,
    'MAX_ZOOM': 18,
}

SUMMERNOTE_THEME = 'bs4'

SUMMERNOTE_CONFIG = {
    'iframe': True,
    'summernote': {
        'airMode': False,
        'width': '100%',
        'height': '500',
    },
    # 'disable_attachment': True,
}

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = env("HOST_EMAIL")
# EMAIL_HOST_USER = env("FROM_EMAIL")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = '587'
# EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django_ses.SESBackend'
DEFAULT_FROM_EMAIL = env("FROM_EMAIL", default="")
EMAIL_RECIPIENT_LIST = env("EMAIL_RECIPIENT_LIST", default="").split(",")
EMAIL_CONTACT_RECIPIENT_LIST = env("EMAIL_CONTACT_RECIPIENT_LIST", default="").split(",")
EMAIL_ECSA_ADMIN = env("EMAIL_ECSA_ADMIN", default="").split(",")
# These are optional -- if they're set as environment variables they won't
# need to be set here as well
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID', default="")
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY', default="")

# Additionally, if you are not using the default AWS region of us-east-1,
# you need to specify a region, like so:
AWS_SES_REGION_NAME = env('AWS_SES_REGION_NAME', default="")
AWS_SES_REGION_ENDPOINT = env('AWS_SES_REGION_ENDPOINT', default="")

# For Nominatim headers
USER_AGENT = env('USER_AGENT', default="")

HOST = env("HOST", default="http://localhost:8000")

SITE_ID = 1
REVIEW_PUBLISH_UNMODERATED = True


REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    ),
}

PASSWORD_RESET_CONFIRM_URL = '/password-reset/'
ACTIVATION_URL = '/activate/'
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '/password-reset/',
    'EMAIL': {
        'activation': 'accounts.views.ActivationEmail',
        'confirmation': 'accounts.views.ConfirmationEmail',
        'password_reset': 'accounts.views.PasswordResetEmail',
    },
    'SEND_ACTIVATION_EMAIL': True,
}

# OPENID
# LOGIN_URL = '/accounts/login/'
OIDC_SESSION_MANAGEMENT_ENABLE = True
OIDC_USERINFO = 'eucs_platform.oidc_provider_settings.userinfo'


# Swagger
LOGOUT_URL = 'rest_framework:logout'

RECAPTCHA_PUBLIC_KEY = env("RECAPTCHA_PUBLIC_KEY", default="")
RECAPTCHA_PRIVATE_KEY = env("RECAPTCHA_PRIVATE_KEY", default="")

# Machina - search for forum conversations
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': str(Path(__file__).parents[2] / 'whoosh_index'),
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MACHINA_BASE_TEMPLATE_NAME = 'base_forum_new.html'
MACHINA_FORUM_NAME = 'Community Forums'
MACHINA_USER_DISPLAY_NAME_METHOD = 'get_full_name'

MACHINA_DEFAULT_AUTHENTICATED_USER_FORUM_PERMISSIONS = [
    'can_see_forum',
    'can_read_forum',
    'can_start_new_topics',
    'can_reply_to_topics',
    'can_edit_own_posts',
    'can_post_without_approval',
    'can_create_polls',
    'can_vote_in_polls',
    'can_download_file',
]

MACHINA_MARKUP_LANGUAGE = None
MACHINA_MARKUP_WIDGET = 'ckeditor_uploader.widgets.CKEditorUploadingWidget'
MACHINA_PROFILE_AVATARS_ENABLED = False

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_REQUIRE_STAFF = False

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'default_custom',
        'toolbar_default_custom': [
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
        ],
    },
    'frontpage': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent',
                '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat']
        ]
    },
}

# CKEDITOR_5 SECTION
customColorPalette = [
    {
        'color': 'hsl(4, 90%, 58%)',
        'label': 'Red'
    },
    {
        'color': 'hsl(340, 82%, 52%)',
        'label': 'Pink'
    },
    {
        'color': 'hsl(291, 64%, 42%)',
        'label': 'Purple'
    },
    {
        'color': 'hsl(262, 52%, 47%)',
        'label': 'Deep Purple'
    },
    {
        'color': 'hsl(231, 48%, 48%)',
        'label': 'Indigo'
    },
    {
        'color': 'hsl(207, 90%, 54%)',
        'label': 'Blue'
    },
]

CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': ['heading', '|', 'bold', 'italic', 'link',
                    'bulletedList', 'numberedList', 'blockQuote', 'imageUpload', ],

    },
    'extends': {
        'blockToolbar': [
            'paragraph', 'heading1', 'heading2', 'heading3',
            '|',
            'bulletedList', 'numberedList',
            '|',
            'blockQuote',
        ],
        'toolbar': ['heading', '|', 'outdent', 'indent', '|', 'bold', 'italic', 'link', 'underline', 'strikethrough',
        'code','subscript', 'superscript', 'highlight', '|', 'codeBlock', 'sourceEditing', 'insertImage',
                    'bulletedList', 'numberedList', 'todoList', '|',  'blockQuote', 'imageUpload', '|',
                    'fontSize', 'fontFamily', 'fontColor', 'fontBackgroundColor', 'mediaEmbed', 'removeFormat',
                    'insertTable',],
        'image': {
            'toolbar': ['imageTextAlternative', '|', 'imageStyle:alignLeft',
                        'imageStyle:alignRight', 'imageStyle:alignCenter', 'imageStyle:side',  '|'],
            'styles': [
                'full',
                'side',
                'alignLeft',
                'alignRight',
                'alignCenter',
            ]

        },
        'table': {
            'contentToolbar': [ 'tableColumn', 'tableRow', 'mergeTableCells',
            'tableProperties', 'tableCellProperties' ],
            'tableProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            },
            'tableCellProperties': {
                'borderColors': customColorPalette,
                'backgroundColors': customColorPalette
            }
        },
        'heading' : {
            'options': [
                { 'model': 'paragraph', 'title': 'Paragraph', 'class': 'ck-heading_paragraph' },
                { 'model': 'heading1', 'view': 'h1', 'title': 'Heading 1', 'class': 'ck-heading_heading1' },
                { 'model': 'heading2', 'view': 'h2', 'title': 'Heading 2', 'class': 'ck-heading_heading2' },
                { 'model': 'heading3', 'view': 'h3', 'title': 'Heading 3', 'class': 'ck-heading_heading3' }
            ]
        }
    },
    'list': {
        'properties': {
            'styles': 'true',
            'startIndex': 'true',
            'reversed': 'true',
        }
    }
}

# END CKEDITOR_5 SECTION

CRON_CLASSES = [
    "eucs_platform.cron.ExpiredUsersCronJob",
    "eucs_platform.cron.NewForumResponseCronJob",
]

CRONJOBS = [
    ('0 1 * * *', 'eucs_platform.cron.ExpiredUsersCronJob'),
    ('0 * * * *', 'eucs_platform.cron.NewForumResponseCronJob')
]


GRAPH_MODELS = {
    'all_applications': True,
    'group_models': True,
}

# For OSX
if platform.system() == 'Darwin':
    GDAL_LIBRARY_PATH = '/opt/homebrew/opt/gdal/lib/libgdal.dylib'
    GEOS_LIBRARY_PATH = '/opt/homebrew/opt/geos/lib/libgeos_c.dylib'

import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for isp project.

Generated by 'django-admin startproject' using Django 1.8.12.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))



STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

MEDIA_ROOT = 'media'
MEDIA_URL = '/media/'


STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jay-a-pocdb(6tu9)%$^p=rue7zuk5c8%8-aj%&lxd22=7+u#3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER  = 'abungaphares@gmail.com'
EMAIL_HOST_PASSWORD = 'rggfcbgttvijille'
EMAIL_PORT = 587
EMAIL_USE_TLS = False

# Application definition

ROOT_URLCONF = 'isp.urls'

WSGI_APPLICATION = 'isp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = False

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'isp', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',
                'aldryn_boilerplates.context_processors.boilerplate',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'aldryn_boilerplates.template_loaders.AppDirectoriesLoader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

INSTALLED_APPS = (

    'djangocms_admin_style',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_image',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'reversion',
    'django.contrib.humanize',
    'crispy_forms',
    'isp',

    # 'cmsplugin_css_background',
    # 'aldryn_boilerplates',
    # 'aldryn_apphooks_config',
    # 'aldryn_categories',
    # 'aldryn_common',
    # 'aldryn_newsblog',
    # 'aldryn_people',
    # 'aldryn_reversion',
    # 'aldryn_translation_tools',
    # 'parler',
    # 'sortedm2m',
    # 'taggit',

)

LANGUAGES = [    ('en', 'English'),]



CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (

        ('home.html', 'home template'),
        ('about.html', 'about template'),
        ('partner.html', 'partner template'),
        ('solution.html', 'solution template'),
        ('contact.html', 'contact template'),
        ('service.html', 'service template'),
        ('career.html', 'career template'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'element_background_image': {
        'plugins': ['CssBackgroundPlugin'],
        'limits': {
            'global': 1,
        },
    },
}

DISABLE_COLLECTSTATIC=1

'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'cmsdb2',
        'PASSWORD': 'ph4re5',
        'PORT': '5432',
        'USER': 'phares',
    }
}
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'ec2-54-247-175-255.eu-west-1.compute.amazonaws.com',
        'NAME': 'ddv7m3leqnr3uv',
        'PASSWORD': '8f49c3d36cb70e4b1e5840bea568eb810399445534df147fc15773622d918b4d',
        'PORT': '5432',
        'USER': 'rllkwgpkyibomg',
    }
}


MIGRATION_MODULES = {
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
}

THUMBNAIL_PROCESSORS = (
    #'easy_thumbnails.processors.colorspace',
    #'easy_thumbnails.processors.autocrop',
    #'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    #'easy_thumbnails.processors.filters'

    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    # 'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
    'easy_thumbnails.processors.background',
)

#MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'




ALDRYN_BOILERPLATE_NAME = 'bootstrap3'
CRISPY_TEMPLATE_PACK = 'bootstrap3'

ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
LOGIN_REDIRECT_URL = '/'

FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")


STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'aldryn_boilerplates.staticfile_finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]


TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "templates"),
    #                                                     missing parens ---------^
)
from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('SECRET_KEY', 'unsafe-default-key')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

_allowed_hosts = os.getenv('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [h for h in _allowed_hosts.split(',') if h] or ['localhost', '127.0.0.1']

# ============================================================
# Jazzmin — Chiroyli admin panel sozlamalari
# ============================================================
JAZZMIN_SETTINGS = {
    "site_title": "Andijon SSB Admin",
    "site_header": "Andijon SSB",
    "site_brand": "Boshqaruv paneli",
    "site_logo": None,
    "login_logo": None,
    "site_icon": None,
    "welcome_sign": "Xush kelibsiz! Andijon viloyati SSB boshqaruv paneliga",
    "copyright": "Andijon viloyati sog'liqni saqlash boshqarmasi",
    "search_model": [],
    "user_avatar": None,

    # Yuqori menyu
    "topmenu_links": [
        {"name": "Saytni ko'rish", "url": "/", "new_window": True, "icon": "fas fa-globe"},
        {"name": "Qo'llanma", "url": "/qollanma/", "new_window": True, "icon": "fas fa-book"},
        {"model": "auth.user"},
    ],

    # Foydalanuvchi menyusi (o'ng yuqori)
    "usermenu_links": [
        {"name": "Saytni ko'rish", "url": "/", "new_window": True},
    ],

    # Yon menyu ko'rsatish
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],

    # Yon menyuni to'liq sozlash — guruhlab, ikonkali
    "order_with_respect_to": [
        "core",
        "news",
        "leadership",
        "structure",
        "documents",
        "contact",
        "auth",
    ],

    "icons": {
        # Core
        "core.generalinfo":     "fas fa-info-circle",
        "core.sitesettings":    "fas fa-palette",
        "core.banner":          "fas fa-images",
        "core.navitem":         "fas fa-bars",
        "core.footerlink":      "fas fa-link",
        "core.pagesection":     "fas fa-th-large",
        "core.mediaasset":      "fas fa-photo-video",
        # News
        "news.news":            "fas fa-newspaper",
        "news.category":        "fas fa-tag",
        # Leadership
        "leadership.leader":    "fas fa-user-tie",
        "leadership.position":  "fas fa-briefcase",
        # Structure
        "structure.department": "fas fa-sitemap",
        # Documents
        "documents.document":        "fas fa-file-alt",
        "documents.documentcategory": "fas fa-folder",
        # Contact
        "contact.appeal":       "fas fa-envelope-open-text",
        # Auth
        "auth.user":            "fas fa-users",
        "auth.group":           "fas fa-user-shield",
    },

    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # Ranglar
    "related_modal_active": True,
    "custom_css": None,
    "custom_js": None,
    "use_google_fonts_cdn": False,
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },

    # Dashboard kartochkalari
    "show_required_indicator": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": "navbar-primary",
    "accent": "accent-primary",
    "navbar": "navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

# ============================================================
# INSTALLED_APPS — jazzmin django.contrib.admin DAN OLDIN bo'lishi shart!
# ============================================================
INSTALLED_APPS = [
    'jazzmin',                          # <- ENG BIRINCHI!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'corsheaders',

    # Local apps
    'apps.core',
    'apps.leadership',
    'apps.structure',
    'apps.documents',
    'apps.news',
    'apps.contact',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

_cors_origins = os.getenv('CORS_ALLOWED_ORIGINS', '')
CORS_ALLOWED_ORIGINS = [o for o in _cors_origins.split(',') if o] or ['http://localhost:3000', 'http://127.0.0.1:3000']

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL', f"sqlite:///{BASE_DIR / 'db.sqlite3'}"),
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

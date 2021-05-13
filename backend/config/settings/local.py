from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vk(e%d&e-!4p2(+oh-e7i+@qxf_g9-hwmc5exw_8gliu^sz!xz"

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "todotu",
#         "USER": "todotu",
#         "PASSWORD": "todotu",
#         "HOST": "localhost",
#         "PORT": 5432,
#     }
# }

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

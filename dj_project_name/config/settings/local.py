from .base import *
import environ

root = environ.Path(__file__) - 3
env = environ.Env()
environ.Env.read_env(root.path('local.env')())

DEBUG = True

DATABASES = {
        'default': env.db()
        }

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

from .base import *

# ************

import os
env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']

# ************

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

ALLOWED_HOSTS = ['www.uptheantics.co.uk']
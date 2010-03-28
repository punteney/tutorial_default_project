import os

##################
# Importing the appropriate settings file for this environment
##################
ENVIRONMENT = os.getenv("DJANGO_ENVIRONMENT")

if ENVIRONMENT == 'production':
    from production import *
elif ENVIRONMENT == 'staging':
    from staging import *
else:
    from dev import *

try:
    from local import *
except ImportError:
    # No local settings which is fine
    pass

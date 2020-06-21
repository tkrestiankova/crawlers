# __init__.py

from .. import settings
from . import helpers


_, CRAWLERS_DB_SESSION, CRAWLERS_BASE = helpers.create_db(settings.DB_URL)

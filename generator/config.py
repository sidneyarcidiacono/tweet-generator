"""Create Config class for environment variable setup."""
import os


class Config(object):

    MONGO_URI = os.getenv("MONGO_URI")

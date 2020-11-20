"""Create Config class for environment variable setup."""
import os


class Config(object):
    """Class config for environment variables."""

    MONGO_URI = os.getenv("MONGO_URI")

import os
import configparser
from configparser import NoOptionError, NoSectionError


dir = os.path.dirname(__file__)


class Config:
    path = "config.ini"
    config = ''

    @staticmethod
    def load():
        Config.config = configparser.ConfigParser()
        Config.config.read(Config.path)

    @staticmethod
    def get(section, item):
        return Config.config[section][item].format()

    @staticmethod
    def get_int(section, item):
        try:
            return Config.config.getint(section, item)
        except NoSectionError as e:
            return e
        except NoOptionError as e:
            return e

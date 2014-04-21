__all__ = ["ConfigObject", "Section", "Settings"]

from ConfigParser import RawConfigParser
import os

DEFAULT_CONFIG = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    "config/default.ini"
)


class ConfigObject(object):
    __slots__ = ["data"]

    def __init__(self):
        self.data = {}

    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
        obj_name = self.__class__.__name__
        raise AttributeError("%r object has no attribute %r" % (obj_name, name))

    def __dir__(self):
        return self.__slots__ + self.data.keys()


class Section(ConfigObject):
    __slots__ = ["name", "data"]

    def __init__(self, name, data):
        self.data = {}
        self.name = name
        # try to auto convert the values
        for name, value in data:
            if value.isdigit():
                value = int(value)
            elif value.lower() == "true":
                value = True
            elif value.lower() == "false":
                value = False
            elif "." in value:
                try:
                    value = float(value)
                except ValueError:
                    pass
            self.data[name] = value


class Settings(ConfigObject):
    __slots__ = ["config_file", "data"]

    def __init__(self, config_file):
        self.data = {}
        self.config_file = config_file
        config = RawConfigParser(allow_no_value=True)
        config.read([DEFAULT_CONFIG, config_file])
        for section in config.sections():
            self.data[section] = Section(section, config.items(section))

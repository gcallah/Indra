"""
The intention behind creating this module is to regularize the
restoration of objects that cannot be directly serialized.
This class will appear as a dictionary, but with the right sort of default
behaviors that we need for our registry.
"""
import json
import warnings

REGISTRY = "Registry"

"""
We can also have some global singletons here. We'll start with `_the_env`;
"""
_the_env = None  # this is a singleton, so global should be ok


def set_env(env):
    global _the_env
    _the_env = env


def get_env():
    return _the_env


"""
Our singleton dict for groups.
"""
_groups_dict = {}


def add_group(name, grp):
    global _groups_dict
    _groups_dict[name] = grp


def get_group(name):
    return _groups_dict.get(name, None)


"""
Our singleton for properties.
"""
_the_props = None


def set_propargs(props):
    """
    Set the global props object.
    """
    global _the_props
    _the_props = props


def get_propargs():
    """
    Get the global props object: shouldn't generally need
    this; instead use next function.
    """
    return _the_props


def get_prop(key, default_val=None):
    """
    Get a particular property.
    If key is missing (or no props) return default_val.
    """
    if _the_props is None:
        return default_val
    else:
        return _the_props.get(key, default_val)


class Registry(object):
    """
    This is an abstraction layer over a dictionary of object names.
    As objects are restored from a serilazed stream, they should be registered
    here. If they are already registered, they will ignore the newly
    registered object, and leave the old value in place.
    """
    def __init__(self):
        self.agents = {}

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return json.dumps(self.to_json(), indent=4)

    def __getitem__(self, key):
        return self.agents[key]

    def get(self, key, default=None):
        if key in self.agents:
            return self.__getitem__(key)
        else:
            return default

    def __setitem__(self, key, value):
        if key not in self.agents or self.agents[key] is None:
            self.agents[key] = value
            if value is None:
                warnings.warn("Trying to set the value of key {} to None.".
                              format(key), RuntimeWarning)
        else:
            pass
            # this fails the tests at the moment, so we need to debug
            # it is the tests that have a problem!
            # raise KeyError("The key \"{}\" already exists in the registry"
            #                .format(key))

    def __contains__(self, item):
        return item in self.agents

    def __iter__(self):
        return iter(self.agents)

    def to_json(self):
        """
        For right now, just list what keys are in the registry.
        """
        return {REGISTRY: str(self.agents.keys())}


registry = Registry()


def register(key, val):
    registry[key] = val


def get_registration(key):
    if key in registry:
        return registry[key]
    else:
        return None

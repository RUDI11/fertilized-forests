## Author: Christoph Lassner

from collections import OrderedDict

class Instantiation(object):
    r"""
    Represents the instantiation with a certain configuration of template
    parameters.
    
    Parameters
    ==========

    types : OrderedDict(string, CppType)
      The C++ template argument names and associated types.
    """
    def __init__(self, type_config_dict):
        assert isinstance(type_config_dict, OrderedDict), "An OrderedDict " +\
          "is required for an Instantiation!"
        self._TypeConfig = type_config_dict
        self._TypesString = "_".join([repr(type) for type in types])

    def __eq__(self, other):
        return self.TypesString == other.TypesString

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return self.TypesString

    def __repr__(self):
        return self.TypesString

    def __hash__(self):
        return hash(self.TypesString)

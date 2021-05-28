from .Errors import *


class Registry:

    def __init__(self):
        self.element_dict = {}

    def add(self, element):
        if element.key() not in self.keys():
            self.element_dict[element.key()] = element
        else:
            raise AlreadyExistError("Try add car that already exist")

    def __getitem__(self, item):
        return self.element_dict[item]

    def keys(self, used=None):
        if used is not None:
            return [v.key() for k, v in self.element_dict.items() if v.used is used]
        else:
            return [v.key() for k, v in self.element_dict.items()]

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class SizeCheck:

    def __init__(self, size_limit, massage = None):
        self.size_limit = size_limit
        self.massage = massage

    @property
    def massage(self):
        return self.__massage

    @massage.setter
    def massage(self, value):
        if value is None:
            self.__massage = f"This file is too big - {value} MB, max is {self.size_limit} MB"
        else:
            self.__message = value

    def __call__(self, value):
        if self.size_limit * 1048 * 1048 < value.size:
            raise ValidationError(self.__massage)




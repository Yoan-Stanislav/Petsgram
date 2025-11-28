from django.db import models
from django.utils.deconstruct import deconstructible


@deconstructible
class SizeCheck(models.Model):

    def __init__(self, size_limit, massage):
        self.size_limit = size_limit
        self.massage = massage

    @property
    def massage(self):
        return self.__massage

    @massage.setter
    def massage(self, value):
        if value is None
            self.__massage = f"This file is too big - {value} MB"

        self.__massage = value

    def __call__(self, size_limit):
        if size_limit >



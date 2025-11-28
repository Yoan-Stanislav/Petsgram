from django.db import models
from photos.validators import SizeCheck
# Create your models here.

class Photos(models.Model):
    photo = models.ImageField(
        validators=[SizeCheck(5)],

    )
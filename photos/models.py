from django.core.validators import MaxLengthValidator
from django.db import models
from photos.validators import SizeCheck
# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(
        validators=[SizeCheck(100)],
        upload_to = 'files'

    )
    description = models.TextField(
        max_length=300,
        validators=[MaxLengthValidator(10)],
        blank = True,
        null = True,
    )

    location = models.CharField(
        max_length=30,
        blank = True,
        null = True,
    )

    tagged_pets = models.ManyToManyField(
        to = "pets.Pet",
        blank = True,
    )

    date_of_publication = models.DateField(
        auto_now = True
    )
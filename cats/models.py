from django.db import models
from django.core import validators

class Breed(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Cat(models.Model):
    nickname = models.CharField(max_length=50, validators=[validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE)
    foods = models.CharField(max_length=100)
    weight = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nickname

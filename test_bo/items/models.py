from random import choice
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Items(models.Model):
    pick = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    result = models.CharField(max_length=10)

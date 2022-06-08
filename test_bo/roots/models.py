from django.db import models


class Roots(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    roots = models.TextField()

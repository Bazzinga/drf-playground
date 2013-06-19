from django.db import models


class MyModel(models.Model):
    x = models.CharField(max_length=32)
    y = models.IntegerField()

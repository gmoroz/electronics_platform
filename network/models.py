from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.PositiveSmallIntegerField()



from djmoney.models.fields import MoneyField
from django.db import models

import moneyed


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.PositiveSmallIntegerField()


class Contact(models.Model):
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class NetworkObj(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    provider = models.ForeignKey(..., on_delete=models.CASCADE)
    debt = MoneyField(
        decimal_places=2, default=0, default_currency="RUR", max_digits=11
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Network(models.Model):
    ...

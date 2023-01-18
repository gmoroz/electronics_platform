from djmoney.models.fields import MoneyField
from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"
w

class Contact(models.Model):
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакт"


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class NetworkObj(models.Model):
    name = models.CharField(max_length=50)
    contacts = models.ForeignKey(Contact, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    employees = models.ForeignKey(Employee, on_delete=models.CASCADE)
    debt = MoneyField(
        decimal_places=2, default=0, default_currency="RUR", max_digits=11
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Factory(NetworkObj):
    pass

    class Meta:
        verbose_name = "Завод"


class Distributor(NetworkObj):
    provider = models.ForeignKey(Factory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Дистрибьютор"


class Dealership(NetworkObj):
    provider = models.ForeignKey(Distributor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Диллерский центр"


class RetailChain(NetworkObj):
    provider = models.ForeignKey(Dealership, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Розничная сеть"


class Businessman(NetworkObj):
    provider = models.ForeignKey(RetailChain, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Индивидуальный предприниматель"


class Network(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)
    retail_chain = models.ForeignKey(RetailChain, on_delete=models.CASCADE)
    business_man = models.ForeignKey(Businessman, on_delete=models.CASCADE)

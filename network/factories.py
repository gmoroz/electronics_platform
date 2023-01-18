import random
import decimal
import factory
from factory.django import DjangoModelFactory

from network import models as net_models


class AddressFactory(DjangoModelFactory):
    country = factory.Faker("country")
    city = factory.Faker("city")
    street = factory.Faker("street_name")
    house_number = factory.Faker("building_number")

    class Meta:
        model = net_models.Address


class ContactFactory(DjangoModelFactory):
    email = factory.Faker("country")
    address = factory.SubFactory(AddressFactory)

    class Meta:
        model = net_models.Contact


class ProductFactory(DjangoModelFactory):
    name = factory.Faker("sentence", nb_words=3, variable_nb_words=True)
    model = factory.Faker("sentence", nb_words=2, variable_nb_words=True)
    release_date = factory.Faker("past_date")

    class Meta:
        model = net_models.Product


class EmployeeFactory(DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = net_models.Employee


class NetworkObjFactory(DjangoModelFactory):
    name = factory.Faker("sentence", nb_words=2, variable_nb_words=True)
    contacts = factory.SubFactory(ContactFactory)
    products = factory.SubFactory(ProductFactory)
    employees = factory.SubFactory(EmployeeFactory)
    debt = decimal.Decimal(random.randrange(2000, 1000000)) / 100

    class Meta:
        model = net_models.NetworkObj
        abstract = True


class PlantFactory(NetworkObjFactory):
    class Meta:
        model = net_models.Plant

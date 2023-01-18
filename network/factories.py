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
    name = factory.Faker("company")
    model = factory.Faker("company")
    release_date = factory.Faker("past_date")

    class Meta:
        model = net_models.Product


class EmployeeFactory(DjangoModelFactory):
    name = factory.Faker("name")

    class Meta:
        model = net_models.Employee


class NetworkObjFactory(DjangoModelFactory):
    name = factory.Faker("company")
    debt = decimal.Decimal(random.randrange(50000, 1000000)) / 100

    @factory.post_generation
    def employees(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for employee in extracted:
                self.employees.add(employee)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.add(product)

    @factory.post_generation
    def contacts(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for contact in extracted:
                self.contacts.add(contact)

    class Meta:
        model = net_models.NetworkObj
        abstract = True


class PlantFactory(NetworkObjFactory):
    class Meta:
        model = net_models.Plant

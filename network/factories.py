import random
import factory
import factory.fuzzy
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
    contacts = factory.RelatedFactoryList(
        ContactFactory, size=lambda: random.randint(2, 5)
    )
    products = factory.RelatedFactoryList(
        ProductFactory, size=lambda: random.randint(25, 75)
    )
    employees = factory.RelatedFactoryList(
        EmployeeFactory, size=lambda: random.randint(50, 100)
    )
    debt_value = factory.fuzzy.FuzzyDecimal(10000.00, 1000000.00)

    @factory.post_generation
    def contacts(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for contact in extracted:
                self.contacts.add(contact)

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.add(product)

    @factory.post_generation
    def employees(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for employee in extracted:
                self.employees.add(employee)

    class Meta:
        abstract = True


class PlantFactory(NetworkObjFactory):
    class Meta:
        model = net_models.Plant


class DistributorFactory(NetworkObjFactory):
    provider = factory.SubFactory(PlantFactory)

    class Meta:
        model = net_models.Distributor


class DealershipFactory(NetworkObjFactory):
    provider = factory.SubFactory(DistributorFactory)

    class Meta:
        model = net_models.Dealership


class RetailChainFactory(NetworkObjFactory):
    provider = factory.SubFactory(DealershipFactory)

    class Meta:
        model = net_models.RetailChain


class BusinessmanFactory(NetworkObjFactory):
    name = factory.Faker("name")
    provider = factory.SubFactory(RetailChainFactory)

    class Meta:
        model = net_models.Businessman



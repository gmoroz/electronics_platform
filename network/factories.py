import random
import decimal
import factory
from factory.django import DjangoModelFactory

from network import models as net_models


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
            for contact in extracted[:3]:
                self.contacts.add(contact)

    class Meta:
        model = net_models.NetworkObj
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


class NetworkFactory(DjangoModelFactory):
    plant = factory.SubFactory(PlantFactory)
    distributor = factory.SubFactory(DistributorFactory)
    dealership = factory.SubFactory(DealershipFactory)
    retail_chain = factory.SubFactory(RetailChainFactory)
    business_man = factory.SubFactory(BusinessmanFactory)

    class Meta:
        model = net_models.Network

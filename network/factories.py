import factory
from factory.django import DjangoModelFactory

from network.models import Address


class AddressFactory(DjangoModelFactory):
    country = factory.Faker("country")
    city = factory.Faker("city")
    street = factory.Faker("street_name")
    house_number = factory.Faker("building_number")

    class Meta:
        model = Address

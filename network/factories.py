import factory
from factory.django import DjangoModelFactory

from models import Address


class AddressFactory(DjangoModelFactory):
    country = factory.Faker("country")
    city = factory.Faker("city")
    street = factory.Faker("street")
    house_number = factory.Faker("building_number")

    class Meta:
        model = Address


a = AddressFactory()
print(a.country)

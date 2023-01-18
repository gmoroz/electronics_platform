from django.db import transaction
from django.core.management.base import BaseCommand

from network.factories import (
    PlantFactory,
    EmployeeFactory,
    ProductFactory,
    ContactFactory,
)

NETWORKS_COUNT = 5
EMPLOYEES_COUNT = NETWORKS_COUNT * 50
PRODUCTS_COUNT = NETWORKS_COUNT * 75
CONTACTS_COUNT = NETWORKS_COUNT * 3


class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Creating new data...")
        employees = [EmployeeFactory() for _ in range(EMPLOYEES_COUNT)]
        products = [ProductFactory() for _ in range(PRODUCTS_COUNT)]
        contacts = [ContactFactory() for _ in range(CONTACTS_COUNT)]

        for _ in range(NETWORKS_COUNT):
            PlantFactory.create(
                employees=employees[:75],
                products=products[:50],
                contacts=contacts[:3],
            )

            del employees[:75]
            del products[:50]
            del contacts[:3]

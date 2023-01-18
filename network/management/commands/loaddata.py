# setup_test_data.py
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from network.factories import PlantFactory, EmployeeFactory, ProductFactory


NETWORKS_COUNT = 5
EMPLOYEES_COUNT = NETWORKS_COUNT * 50
PRODUCTS_COUNT = NETWORKS_COUNT * 75


class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Creating new data...")
        employees = [EmployeeFactory() for _ in range(EMPLOYEES_COUNT)]
        products = [ProductFactory() for _ in range(PRODUCTS_COUNT)]

        for _ in range(NETWORKS_COUNT):
            plant = PlantFactory()
            plant.employees.add(*employees[:75])
            plant.products.add(*products[:75])
            del employees[:75]
            del products[:75]

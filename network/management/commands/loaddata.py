# setup_test_data.py
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from network.factories import PlantFactory


NETWORKS_COUNT = 5


class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Creating new data...")
        for _ in range(NETWORKS_COUNT):
            PlantFactory()

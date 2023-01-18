# setup_test_data.py
import random

from django.db import transaction
from django.core.management.base import BaseCommand

from network.models import *
from network.factories import AddressFactory

ADDRES

class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Creating new data...")
        for _ in range(NUM_USERS):
            address = AddressFactory()


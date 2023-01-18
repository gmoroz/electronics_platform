from django.db import transaction
from django.core.management.base import BaseCommand

from network.factories import BusinessmanFactory
from network.models import Network

NETWORKS_COUNT = 5


class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Creating new data...")

        for _ in range(NETWORKS_COUNT):
            businesman = BusinessmanFactory()
            Network.objects.create(
                plant=businesman.provider.provider.provider.provider,
                distributor=businesman.provider.provider.provider,
                dealership=businesman.provider.provider,
                retail_chain=businesman.provider,
                business_man=businesman,
            )
        self.stdout.write("Data created succefully")

from django.db import transaction
from django.core.management.base import BaseCommand

from network.factories import (
    BusinessmanFactory,
    ContactFactory,
    PlantFactory,
    EmployeeFactory,
    ProductFactory,
    RetailChainFactory,
)
from network.models import Network

NETWORKS_COUNT = 5
CONTACTS_COUNT = 3
EMPLOYEES_COUNT = 50
PRODUCTS_COUNT = 75


class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):

        self.stdout.write("Creating new data...")
        try:
            for i in range(NETWORKS_COUNT):
                
                print(f"{i+1}/{NETWORKS_COUNT}")
                
                plant = PlantFactory.create(
                    contacts=(ContactFactory() for _ in range(CONTACTS_COUNT)),
                    employees=(EmployeeFactory() for _ in range(EMPLOYEES_COUNT)),
                    products=(ProductFactory() for _ in range(PRODUCTS_COUNT)),
                )
                factories = [plant]
                factories_models = [RetailChainFactory, BusinessmanFactory]
                for_network = [plant]
                
                for ModelFactory in factories_models:
                    new_model = ModelFactory.create(
                        contacts=(ContactFactory() for _ in range(CONTACTS_COUNT)),
                        employees=(EmployeeFactory() for _ in range(EMPLOYEES_COUNT)),
                        products=(ProductFactory() for _ in range(PRODUCTS_COUNT)),
                        provider=factories.pop(),
                    )
                    for_network.append(new_model)
                    factories.append(new_model)

                Network.objects.create(
                    plant=for_network[0],
                    retail_chain=for_network[1],
                    businessman=for_network[2],
                )

        except Exception as e:
            self.stdout.write(
                "Something went wrong. Check this exception, google it, etc:\n\n{}".format(
                    e
                )
            )
        else:
            self.stdout.write("Data created and writed to db succefully!")

from rest_framework import serializers

from . import models as net_models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Address
        fields = "__all__"
        read_only_fields = ("id",)


class ContactSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = net_models.Contact
        fields = "__all__"
        read_only_fields = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Product
        fields = "__all__"
        read_only_fields = ("id",)


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Employee
        fields = "__all__"
        read_only_fields = ("id",)


class NetworkObjList(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    products = ProductSerializer(many=True)
    employees = EmployeeSerializer(many=True)

    def is_valid(self, *, raise_exception=False):
        self._contacts = self.initial_data["contacts"]
        self._products = self.initial_data["products"]
        self._employees = self.initial_data["employees"]
        return super().is_valid(raise_exception=raise_exception)

    def _prepare_data(self, validated_data):
        contacts = []
        for contact_instance in self._contacts:
            address_data = contact_instance["address"]
            address, _ = net_models.Address.objects.get_or_create(
                country=address_data["country"],
                city=address_data["city"],
                street=address_data["street"],
                house_number=address_data["house_number"],
            )
            contact, _ = net_models.Contact.objects.get_or_create(
                email=contact_instance["email"], address=address
            )
            contacts.append(contact)

        products = []
        for product_instance in self._products:
            product, _ = net_models.Product.objects.get_or_create(
                name=product_instance["name"],
                model=product_instance["model"],
            )
            products.append(product)

        employees = []
        for employee_instance in self._employees:
            employee, _ = net_models.Employee.objects.get_or_create(
                name=employee_instance["name"]
            )
            employees.append(employee)

        return contacts, products, employees

    class Meta:
        model = net_models.NetworkObj
        abstract = True
        fields = ("name", "provider_name", "debt")
        read_only_fields = ("id",)


class PlantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Plant
        fields = ("name", "created_at", "id")


class PlantSerializer(NetworkObjList):
    def create(self, validated_data):
        contacts, products, employees = super()._prepare_data(validated_data)
        plant = net_models.Plant.objects.create(name=validated_data["name"])
        plant.contacts.set(contacts)
        plant.products.set(products)
        plant.employees.set(employees)

        plant.save()
        return plant
   
        
    class Meta:
        model = net_models.Plant
        read_only_fields = ("created_at", "id")
        fields = "__all__"

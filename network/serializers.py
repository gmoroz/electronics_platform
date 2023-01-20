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


class NetworkObjBaseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    products = ProductSerializer(many=True)
    employees = EmployeeSerializer(many=True)

    def _prepare_data(self, validated_data):
        self._contacts = validated_data.get("contacts", [])
        self._products = validated_data.get("products", [])
        self._employees = validated_data.get("employees", [])
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

    def update(self, instance, validated_data):
        contacts, products, employees = self._prepare_data(validated_data)
        instance.name = validated_data.get("name", instance.name)

        if contacts:
            instance.contacts.set(contacts)
        if products:
            instance.products.set(products)
        if employees:
            instance.employees.set(employees)

        instance.save()
        return instance

    class Meta:
        model = net_models.NetworkObj
        abstract = True
        fields = ("name", "provider_name", "debt")
        read_only_fields = ("id",)


class PlantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Plant
        fields = ("name", "created_at", "id")


class PlantSerializer(NetworkObjBaseSerializer):
    def create(self, validated_data):
        contacts, products, employees = self._prepare_data(validated_data)
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


class RetailChainListSerializer(serializers.ModelSerializer):
    provider = PlantListSerializer()

    class Meta:
        model = net_models.RetailChain
        fields = ("name", "created_at", "id", "provider")


class RetailChainSerializer(NetworkObjBaseSerializer):
    provider = PlantSerializer()
    debt = serializers.CharField()

    def create(self, validated_data):
        contacts, products, employees = self._prepare_data(validated_data)
        provider = PlantSerializer().create(
                validated_data=validated_data["provider"]
            )

        retail_chain = net_models.RetailChain.objects.create(
            name=validated_data["name"],
            debt_value=validated_data["debt"],
            provider=provider,
        )
        retail_chain.contacts.set(contacts)
        retail_chain.products.set(products)
        retail_chain.employees.set(employees)

        retail_chain.save()
        return retail_chain



    class Meta:
        model = net_models.RetailChain
        exclude = ("debt_value",)

from rest_framework import serializers

from . import models as net_models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Address
        fields = "__all__"


class ContactSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = net_models.Contact
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Product
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Employee
        fields = "__all__"


class NetworkObjList(serializers.ModelSerializer):
    class Meta:
        model = net_models.NetworkObj
        abstract = True
        fields = ("name", "provider_name", "debt")


class PlantList(serializers.ModelSerializer):
    class Meta:
        model = net_models.Plant
        fields = ("name", "created_at", "id")


class PlantSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    products = ProductSerializer(many=True)
    employees = EmployeeSerializer(many=True)

    class Meta:
        read_only_fields = "created_at"
        fields = "__all__"

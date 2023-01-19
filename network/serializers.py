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


class ProductSerializer(serializers.Model):
    class Meta:
        model = net_models.Product
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Employee
        fields = "__all__"



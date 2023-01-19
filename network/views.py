from rest_framework import serializers
from . import models as net_models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = net_models.Address
        fields = "__all__"


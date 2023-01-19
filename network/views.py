from rest_framework import pagination, viewsets
from . import models as net_models, serializers


class PlantViewSet(viewsets.ModelViewSet):
    queryset = net_models.Plant
    pagination_class = pagination

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.PlantList
        return serializers.PlantSerializer

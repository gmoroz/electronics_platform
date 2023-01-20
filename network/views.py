from rest_framework import pagination, viewsets

from . import models as net_models, serializers


class BasePagination(pagination.PageNumberPagination):
    page_size = 5


class PlantViewSet(viewsets.ModelViewSet):
    queryset = net_models.Plant.objects.all()
    pagination_class = BasePagination

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.PlantListSerializer
        return serializers.PlantSerializer

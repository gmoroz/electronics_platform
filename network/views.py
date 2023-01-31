from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated

from . import models as net_models, serializers


class BasePagination(pagination.PageNumberPagination):
    page_size = 5


class ListWithFilterViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        if country := request.GET.get("country"):
            self.queryset = self.queryset.filter(
                contacts__address__country__exact=country
            )

        return super().list(request, *args, **kwargs)

    class Meta:
        abstract = True


class PlantViewSet(ListWithFilterViewSet):
    queryset = net_models.Plant.objects.all()
    pagination_class = BasePagination
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.PlantListSerializer
        return serializers.PlantSerializer


class RetailChainViewSet(ListWithFilterViewSet):
    queryset = net_models.RetailChain.objects.all()
    pagination_class = BasePagination
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.RetailChainListSerializer
        if self.action == "retrieve":
            return serializers.RetailChainRetrieveSerializer
        return serializers.RetailChainSerializer


class BusinessmanViewSet(ListWithFilterViewSet):
    queryset = net_models.Businessman.objects.all()
    pagination_class = BasePagination
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.BusinessmanListSerializer
        if self.action == "retrieve":
            return serializers.BusinessmanRetrieveSerializer
        return serializers.BusinessmanSerializer

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

    def list(self, request, *args, **kwargs):
        if country := request.GET.get("country"):
            self.queryset = self.queryset.filter(
                contacts__address__country__exact=country
            )

        return super().list(request, *args, **kwargs)


class RetailChainViewSet(viewsets.ModelViewSet):
    queryset = net_models.RetailChain.objects.all()
    pagination_class = BasePagination

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.RetailChainListSerializer
        if self.action == "retrieve":
            return serializers.RetailChainRetrieveSerializer
        return serializers.RetailChainSerializer

    def list(self, request, *args, **kwargs):
        if country := request.GET.get("country"):
            self.queryset = self.queryset.filter(
                contacts__address__country__exact=country
            )

        return super().list(request, *args, **kwargs)


class BusinessmanViewSet(viewsets.ModelViewSet):
    queryset = net_models.Businessman.objects.all()
    pagination_class = BasePagination

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.BusinessmanListSerializer
        if self.action == "retrieve":
            return serializers.BusinessmanRetrieveSerializer
        return serializers.BusinessmanSerializer

    def list(self, request, *args, **kwargs):
        if country := request.GET.get("country"):
            self.queryset = self.queryset.filter(
                contacts__address__country__exact=country
            )

        return super().list(request, *args, **kwargs)

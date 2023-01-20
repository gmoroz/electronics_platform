from rest_framework.routers import SimpleRouter
from django.urls import path

from network import views

network_router = SimpleRouter()
network_router.register("plants", views.PlantViewSet, basename="plants")
network_router.register("retailchains", views.RetailChainViewSet, basename="retailchains")
network_router.register("businessmen", views.BusinessmanViewSet, basename="businessmen")

urlpatterns = []

urlpatterns += network_router.urls

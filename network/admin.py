from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from . import models as net_models


@admin.action(description="Set to 0 debt of selected provider(s)")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt_value=0)


@admin.register(net_models.Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "plant_link",
        "distributor_link",
        "dealership_link",
        "retail_chain_link",
        "business_man_link",
    )
    readonly_fields = (
        "plant_link",
        "distributor_link",
        "dealership_link",
        "retail_chain_link",
        "business_man_link",
    )

    def plant_link(self, obj):
        return mark_safe(
            "<a href='{}'>{}</a>".format(
                reverse("admin:network_plant_change", args=(obj.plant.id,)),
                obj.plant.name,
            )
        )

    def distributor_link(self, obj):
        return mark_safe(
            "<a href='{}'>{}</a>".format(
                reverse("admin:network_distributor_change", args=(obj.distributor.id,)),
                obj.distributor.name,
            )
        )

    def dealership_link(self, obj):
        return mark_safe(
            "<a href='{}'>{}</a>".format(
                reverse("admin:network_dealership_change", args=(obj.dealership.id,)),
                obj.dealership.name,
            )
        )

    def retail_chain_link(self, obj):
        return mark_safe(
            "<a href='{}'>{}</a>".format(
                reverse(
                    "admin:network_retailchain_change", args=(obj.retail_chain.id,)
                ),
                obj.retail_chain.name,
            )
        )

    def business_man_link(self, obj):
        return mark_safe(
            "<a href='{}'>{}</a>".format(
                reverse("admin:network_businessman_change", args=(obj.businessman.id,)),
                obj.businessman.name,
            )
        )

    plant_link.short_description = "plant"
    distributor_link.short_description = "distributor"
    dealership_link.short_description = "dealership"
    retail_chain_link.short_description = "retail_chain"
    business_man_link.short_description = "businessman"


class BaseProviderAdmin(admin.ModelAdmin):
    list_filter = ("contacts__address__city",)
    list_display = ("name", "debt")
    actions = (clear_debt,)

    class Meta:
        abstract = True


@admin.register(net_models.Plant)
class PlantAdmin(BaseProviderAdmin):
    pass


class ProviderWithLink(BaseProviderAdmin):
    list_display = ("name", "debt", "provider_link")
    actions = (clear_debt,)
    readonly_fields = ("provider_link",)

    def provider_link(self, obj):
        return mark_safe(
            "<a href='{}'>{}</a>".format(
                reverse(
                    "admin:network_{}_change".format(obj.provider_name),
                    args=(obj.id,),
                ),
                obj.provider.name,
            )
        )

    provider_link.short_description = "provider"


@admin.register(net_models.Distributor)
class DistributorAdmin(ProviderWithLink):
    pass


@admin.register(net_models.Dealership)
class DealershipAdmin(ProviderWithLink):
    pass


@admin.register(net_models.RetailChain)
class RetailChainAdmin(ProviderWithLink):
    pass


@admin.register(net_models.Businessman)
class BusinessmanAdmin(ProviderWithLink):
    pass


admin.site.register(net_models.Address)
admin.site.register(net_models.Product)
admin.site.register(net_models.Employee)

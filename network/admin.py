from django.contrib import admin
from . import models as net_models

admin.site.register(net_models.Address)
admin.site.register(net_models.Plant)

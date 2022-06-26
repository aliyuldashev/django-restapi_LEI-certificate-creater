from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Address)
admin.site.register(models.LEI_user)
admin.site.register(models.Billing_data)
admin.site.register(models.Parent_companies)



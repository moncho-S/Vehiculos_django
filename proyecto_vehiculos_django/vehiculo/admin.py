from django.contrib import admin
from .models import *
# Register your models here.
class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields=('creado','modificado')
    list_display =['marca','modelo','creado','modificado']
    list_filter =['precio']
    search_fields =['marca']
    ordering=('creado','modificado','precio')

admin.site.register(VehiculoModel,VehiculoAdmin)
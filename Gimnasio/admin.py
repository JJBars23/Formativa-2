from django.contrib import admin
from .models import Plan, Socio

# Register your models here.
@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'orden', 'precio_formateado')
    search_fields = ('nombre',)
    list_filter = ('orden',)

    @admin.display(description='Precio', ordering='precio')
    def precio_formateado(self, obj):
        return obj.precio_formateado
    
@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'plan')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('plan',)
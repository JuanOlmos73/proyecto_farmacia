from django.contrib import admin
from .models import medicamentos
from .models import salida_medicamento
# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
admin.site.register(medicamentos,AdministrarModelo)


class AdministrarSalida(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
admin.site.register(salida_medicamento,AdministrarSalida)
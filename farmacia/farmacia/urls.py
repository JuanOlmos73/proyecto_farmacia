"""farmacia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registrofarmacia import views as farma
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',farma.principal_registros,name="principal"),
    path('reg_farmacos/',farma.regitrarfarmacia, name="formulario"),
    path('registrar/',farma.registrar, name="registro"),
    path('salida_farmacos/',farma.salida_farmacos, name="salida_farmacos"),
    path('inventarios/',farma.stock, name="inventario"),
    path('formsreabastecer/<int:id>/',farma.rellenar,name="rellenar"),
    path('editar/<int:id>/',farma.editar,name="editar"),
    path('salidafarmaco/',farma.salidafarmaco,name="salida_farm")
]
if settings.DEBUG:
    from django.conf.urls.static import static 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

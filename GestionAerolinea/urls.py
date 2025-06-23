from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('pasajeros/', include('pasajeros.urls')),
    path('reservas/', include('reservas.urls')),
    path('reportes/', include('reportes.urls')),
    path('flota/', include('flota.urls')),
]

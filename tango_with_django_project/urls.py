from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('rango.urls')),
    path('rango/', include('rango.urls')),
    path('admin/', admin.site.urls),
]

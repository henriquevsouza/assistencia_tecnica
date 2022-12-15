from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('clientes.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('clientes/', include('clientes.urls')),
                  path('servicos/', include('servicos.urls')),
                  path('sobre/', include('sobre.urls')),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







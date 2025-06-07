"""
Configuración de URL para el proyecto de configuración.

La lista `urlpatterns` enruta las URL a las vistas. Para más información, consulte:
https://docs.djangoproject.com/en/5.2/topics/http/urls/
Ejemplos:
Vistas de funciones

1. Agregar una importación: `from my_app import views`

2. Agregar una URL a `urlpatterns`: `path('', views.home, name='home')
Vistas basadas en clases

1. Agregar una importación: `from other_app.views import Home`

2. Agregar una URL a `urlpatterns`: `path('', Home.as_view(), name='home')
Incluir otra URLconf

1. Importar la función `include()`: `from django.urls import include, path`

2. Agregar una URL a `urlpatterns`: `path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from facturacion.views import login_view, registro_view, clientes  # Importa la vista del login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='inicio'),  # Esto muestra el login en "/"
    path('login/', login_view, name='login'),
    path('registro/', registro_view, name='registro'), #registro
    path('clientes/', clientes, name='clientes'),
    path('facturacion/', include('facturacion.urls')),  # Incluye las rutas de la app

]




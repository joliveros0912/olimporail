"""
URL configuration for ApisOlimpo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.decorators import login_required

from django.urls import path,include
from olimpo import views

urlpatterns = [
    path('',views.home),
    path('formularios/', include("formularios.urls")),
    path('administrador/',views.admin),
    path('administrador/',include('administrador.urls')),
    path('amadellaves/',include('amallaves.urls')),
    path('adicionales/',include('meseriyromm.urls')),
    # path('reserva/',include('reserva.urls')),
    path('reservaClient/',include('olimpo.urls')),



    # path('admin/', admin.site.urls),
    # path('apis/',include('apia.urls'))

]

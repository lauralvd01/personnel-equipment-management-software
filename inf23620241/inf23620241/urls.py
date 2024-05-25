"""
URL configuration for inf23620241 project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inf236backend.views import MotorViewSet, CamionViewSet, AsignacionMotorCamionViewSet, handle_incident


router = DefaultRouter()
router.register(r'motor',MotorViewSet)
router.register(r'camion',CamionViewSet)
router.register(r'asignacion',AsignacionMotorCamionViewSet)
urlpatterns = [
    path('', include(router.urls)),
    #path('admin/', admin.site.urls),
    path('api/incidents/', handle_incident, name='handle_incident'), #Path de Vista, linea de prueba
]
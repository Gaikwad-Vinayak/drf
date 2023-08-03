"""apic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.db import router
from django.urls import path,include
from cores import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('stuapi',views.studentapi,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.studentapi.as_view({'get': 'list'})),
    # path('<int:pk>/',views.studentapi.as_view({'get': 'list'})),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]

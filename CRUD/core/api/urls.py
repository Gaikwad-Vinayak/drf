from django.contrib import admin
from django.db import router
from django.urls import path,include
from core.api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'api',views.apiview)

urlpatterns = [
    path('',include(router.urls)),


]
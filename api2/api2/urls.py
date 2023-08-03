
from django.contrib import admin
from django.db import router
from django.urls import path,include
from core import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'api',views.api)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),    
]

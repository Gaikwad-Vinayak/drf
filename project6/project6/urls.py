from django.contrib import admin
from django.urls import path
from pyrsistent import v
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
]

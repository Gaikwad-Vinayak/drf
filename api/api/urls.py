
from django.contrib import admin
from django.db import router
from django.urls import path,include
from core.views import studentapi, teacherapi
from core import views
from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
router=DefaultRouter()
router.register(r'student',views.studentapi)
router.register(r'teacher',views.teacherapi)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]


from django.contrib import admin
from django.db import router
from django.urls import path,include
from core import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenVerifyView,TokenRefreshView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register(r'api',views.apiview,basename='student')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('verify/',TokenRefreshView.as_view()),
]


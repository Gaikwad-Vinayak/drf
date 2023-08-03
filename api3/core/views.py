from django.shortcuts import render
from .serializers import stusiri
from .models import student
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class apiview(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=stusiri
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

from django.shortcuts import render
from rest_framework.mixins import ListModelMixin
from .models import student
from .serializers import stusiri
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
# Create your views here.
class api(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=stusiri
    authentication_classe=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    
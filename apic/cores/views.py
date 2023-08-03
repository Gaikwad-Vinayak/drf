from multiprocessing import AuthenticationError
from django.shortcuts import render
from .models import student
from .serializers import stusiri
from rest_framework import viewsets
from rest_framework.authentication import BaseAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# Create your views here.
class studentapi(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=stusiri
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import student,teachers
from .serializers import studentsiri,teachersiri
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
# Create your views here.
# class LargeResultsSetPagination(PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 3

class studentapi(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studentsiri


class teacherapi(viewsets.ModelViewSet):
    queryset=teachers.objects.all()
    serializer_class=teachersiri
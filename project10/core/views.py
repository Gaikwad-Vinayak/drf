from django.shortcuts import render
from rest_framework.response import Response
from .models import student
from .sirializers import mysiri
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
# Create your views here.
from rest_framework.views import APIView
from django.core.paginator import Paginator

class AccountViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = mysiri
    filterset_fields=['name']
    # search_fields = ['id', 'name']
# class AccountViewSet(ListAPIView,CreateAPIView):
#     queryset = student.objects.all()
#     serializer_class = mysiri

# class AccountViewSetipdate(RetrieveAPIView):
#     queryset = student.objects.all()
#     serializer_class = mysiri


# class EventNewsItems(APIView):

#     def get(self, request, format=None):

#         #user = request.user
#         news = student.objects.all()
#         # news = event.get_news_items().all()

#          # -----------------------------------------------------------
#         page_number = self.request.query_params.get('page_number ', 1)
#         page_size = self.request.query_params.get('page_size ', 10)

#         paginator = Paginator(news , page_size)
#         serializer = mysiri(paginator.page(page_number) , many=True, context={'request':request})
#         # -----------------------------------------------------------

#         response = Response(serializer.data)
#         return response

from rest_framework.pagination import PageNumberPagination

class EventNewsItems(APIView, PageNumberPagination):
    #this will output only 3 objects per page
    page_size = 2
    def get(self, request, format=None):
        news = student.objects.all()
        # news = event.get_news_items().all()

        results = self.paginate_queryset(news, request, view=self)
        serializer = mysiri(results, many=True)
        return self.get_paginated_response(serializer.data)
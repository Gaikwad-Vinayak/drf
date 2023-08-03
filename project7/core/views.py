from django.shortcuts import render

# Create your views here.
def home(request,group_name):
    return render(request,'core/home.html',{'groupname':group_name})
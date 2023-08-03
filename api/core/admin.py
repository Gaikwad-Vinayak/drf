from django.contrib import admin
from .models import student,teachers
# Register your models here.
@admin.register(student)
class adminmodelclass(admin.ModelAdmin):
    list_display=['id','name','roll','city']

@admin.register(teachers)
class adminmodel(admin.ModelAdmin):
    list_display=['id','name','dept','stu']

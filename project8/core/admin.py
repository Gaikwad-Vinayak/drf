from django.contrib import admin
from .models import chat
# Register your models here.
@admin.register(chat)
class admin(admin.ModelAdmin):
    list_display=['id','content','content2']

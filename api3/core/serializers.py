from attr import fields
from rest_framework import serializers
from .models import student
class stusiri(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['name','roll','city']
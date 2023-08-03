from attr import fields
from rest_framework import serializers
from .models import student
class mysiri(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
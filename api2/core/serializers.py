from attr import fields
from rest_framework import serializers
from core.models import student

class stusiri(serializers.ModelSerializer):
    class Meta:
        model=student
        fields='__all__'
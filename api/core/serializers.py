from attr import fields
from rest_framework import serializers
from .models import student,teachers
class studentsiri(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=['name','roll','city']
    
class teachersiri(serializers.Serializer):
    stu = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    class Meta:
        model=teachers
        fields=['name','dept','stu']
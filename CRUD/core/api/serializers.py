from attr import fields
from rest_framework import serializers
from core.models import mode

class crudsiri(serializers.ModelSerializer):
    class Meta:
        model=mode
        fields=['id','name','email','password']
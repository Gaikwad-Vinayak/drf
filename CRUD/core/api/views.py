from core.models import mode
from core.api.serializers import crudsiri
from rest_framework import viewsets

class apiview(viewsets.ModelViewSet):
    queryset=mode.objects.all()
    serializer_class=crudsiri
    

from rest_framework import viewsets 
from .models import MessageUser
from .serializers import MessageUserSerializer
    
class MessageUserViewSet(viewsets.ModelViewSet): 
    queryset = MessageUser.objects.all()
    serializer_class = MessageUserSerializer
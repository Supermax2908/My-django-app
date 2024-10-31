from rest_framework import viewsets 
from .models import MessageUser
from .serializers import MessageUserSerializer
    
class MessageUserViewSet(viewsets.ModelViewSet): 
    queryset = MessageUser.objects.all()
    serializer_class = MessageUserSerializer
    
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)
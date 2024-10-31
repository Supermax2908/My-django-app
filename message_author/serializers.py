from rest_framework.serializers import ModelSerializer, CharField, PrimaryKeyRelatedField
from .models import MessageUser
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['username']
    
class MessageUserSerializer(ModelSerializer):
    author = PrimaryKeyRelatedField(queryset=User.objects.all())
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta: 
        model = MessageUser
        fields = ['author', 'message', 'user', 'is_read', 'created_at']
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import MessageUser
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['username']
    
class MessageUserSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    author = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    
    class Meta: 
        model = MessageUser
        fields = ['author', 'message', 'user', 'is_read', 'created_at']
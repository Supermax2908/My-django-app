from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import Question, Answer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['username']
    
class QuestionSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    
    class Meta: 
        model = Question
        fields = ['question', 'user', 'lesson', 'created_at']
        
        
class AnswerSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    answerer = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    
    class Meta:
        model=Answer
        fields = ['user', 'question', 'answer', 'answerer', 'created_at']
        
        
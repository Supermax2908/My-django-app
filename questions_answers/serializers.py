from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Question, Answer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['username']
    
class QuestionSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta: 
        model = Question
        fields = ['question', 'user', 'lesson', 'created_at']
        
        
class AnswerSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    answerer = PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model=Answer
        fields = ['user', 'question', 'answer', 'answerer', 'created_at']
        
        
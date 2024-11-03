from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
    
class QuestionViewSet(viewsets.ModelViewSet): 
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)
    
class AnswerViewSet(viewsets.ModelViewSet): 
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)
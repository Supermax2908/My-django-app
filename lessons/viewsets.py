from rest_framework import viewsets 
from .models import Lesson, LessonComment 
from .serializers import LessonSerializer, LessonCommentSerializer 
    
class LessonViewSet(viewsets.ModelViewSet): 
    queryset = Lesson.objects.all() 
    serializer_class = LessonSerializer
     
class LessonCommentViewSet(viewsets.ModelViewSet):
    queryset = LessonComment.objects.all() 
    serializer_class = LessonCommentSerializer
from rest_framework import viewsets 
from .models import Lesson, LessonComment 
from .serializers import LessonSerializer, LessonCommentSerializer 
    
class LessonViewSet(viewsets.ModelViewSet): 
    queryset = Lesson.objects.all() 
    serializer_class = LessonSerializer
    permission_classes = []
    authentication_classes = []
    # def get_queryset(self):
    #     user = self.request.user

    #     if user.is_superuser:
    #         return self.queryset
    #     else:
    #         return self.queryset.filter(user=self.request.user)
     
class LessonCommentViewSet(viewsets.ModelViewSet):
    queryset = LessonComment.objects.all() 
    serializer_class = LessonCommentSerializer
    # permission_classes = []
    # authentication_classes = []
    
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)
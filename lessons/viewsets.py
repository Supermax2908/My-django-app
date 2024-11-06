from rest_framework import viewsets 
from .models import Lesson, LessonComment 
from .serializers import LessonSerializer, LessonCommentSerializer 
from django_filters.rest_framework import DjangoFilterBackend
from .filters import LessonFilterSet
from rest_framework.filters import SearchFilter, OrderingFilter

class LessonViewSet(viewsets.ModelViewSet): 
    queryset = Lesson.objects.all() .select_related('category').order_by('uiid')
    serializer_class = LessonSerializer
    
    permission_classes = []
    authentication_classes = []
    filterset_class = LessonFilterSet
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['topic', 'cash']
    ordering_fields = ['topic', 'cash', 'uiid']
     
class LessonCommentViewSet(viewsets.ModelViewSet):
    queryset = LessonComment.objects.all() 
    serializer_class = LessonCommentSerializer
    
    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(user=self.request.user)
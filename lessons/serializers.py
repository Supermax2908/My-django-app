from rest_framework.serializers import ModelSerializer, SlugRelatedField
from .models import LessonTag, LessonCategory, Lesson, LessonComment
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer): 
    class Meta: 
        model = User 
        fields = ['username']

class LessonTagSerializer(ModelSerializer): 
    class Meta: 
        model = LessonTag 
        fields = ['id', 'name'] 

class LessonCategorySerializer(ModelSerializer): 
    class Meta: 
        model = LessonCategory
        fields = ['id', 'name'] 
    
class LessonSerializer(ModelSerializer):
    category = LessonCategorySerializer()
    tag = LessonTagSerializer()
    user = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    author = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    
    class Meta: 
        model = Lesson 
        fields = ['uiid', 'tag', 'category', 'author', 'topic', 'description', 'user', 'cash', 'payment', 'created_at'] 
        
    def create(self, validated_data): 
        tag_data = validated_data.pop('tag') 
        category_data = validated_data.pop('category') 
        
        tag, created = LessonTag.objects.get_or_create(**tag_data) 
        category, created = LessonCategory.objects.get_or_create(**category_data)
        
        lesson = Lesson.objects.create(tag=tag, category=category, **validated_data) 
        return lesson
    
class LessonCommentSerializer(ModelSerializer): 
    lesson = LessonSerializer()
    user = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta: 
        model = LessonComment 
        fields = [ 'id', 'user', 'lesson', 'comment', 'created_at']
from django.db import models
import uuid
import datetime
from django.contrib.auth.models import User
# Create your models here.

class LessonTag(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class LessonCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Lesson(models.Model):
    uiid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    tag = models.ForeignKey('LessonTag', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey('LessonCategory', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_lessons')
    topic = models.CharField(max_length=255)
    description = models.TextField(default=None)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_lessons', default=None)
    cash = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    payment = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Тема уроку: {self.topic} автора {self.author} - {self.cash}'
        
    
class LessonComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    
    comment = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Коментарій від {self.user} під "{self.lesson}"'
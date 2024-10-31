from django.db import models
from django.contrib.auth.models import User
from lessons.models import Lesson
# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.question} від {self.user}'
    
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    answerer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answerer_answer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.answer} від {self.answerer} до {self.user}'
    
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MessageUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_message')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_message')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Повідомлення від {self.author.username} дo {self.user.username}: {self.message}"
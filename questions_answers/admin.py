from django.contrib import admin
from .models import Question, Answer
# Register your models here.

@admin.register(Question)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('id', 'user', 'question', 'created_at')
    ordering = ['question']
    fields = ('id', 'user', 'question', 'created_at')
    readonly_fields = ('id', 'created_at')
    
@admin.register(Answer)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('id', 'user', 'answer', 'question', 'answerer', 'created_at')
    ordering = ['answer']
    fields = ('id', 'user', 'question', 'answerer', 'answer', 'created_at')
    readonly_fields = ('id', 'created_at')
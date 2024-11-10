from django.contrib import admin
from .models import LessonTag, LessonCategory, Lesson, LessonComment
# Register your models here.

@admin.register(LessonTag)
class LessonTagAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name')
    ordering = ('name',)
    fields = ('id', 'name')
    readonly_fields = ('id',)
    
@admin.register(LessonCategory)
class LessonCategoryAdmin(admin.ModelAdmin):
    list_filter = ('id', 'name')
    ordering = ('name',)
    fields = ('id', 'name')
    readonly_fields = ('id',)
    
@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('topic', 'author', 'user', 'cash', 'is_paid', 'created_at', 'updated_at')
    list_filter = ('author', 'user', 'category', 'is_paid')
    search_fields = ('topic', 'author__username', 'user__username') 
    ordering = ('topic', 'author', 'user')
    
@admin.register(LessonComment)
class LessonCommentAdmin(admin.ModelAdmin):
    list_filter = ('id', 'user', 'lesson', 'comment', 'created_at')
    ordering = ('comment',)
    fields = ('id', 'user', 'lesson', 'comment', 'created_at')
    readonly_fields = ('id', 'created_at')
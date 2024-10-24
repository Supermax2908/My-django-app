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
    list_filter = ('uiid', 'tag', 'category', 'author', 'user', 'topic', 'created_at')
    ordering = ('topic',)
    fields = ('uiid', 'tag', 'category', 'author', 'user', 'topic', 'description', 'cash', 'payment')
    readonly_fields = ('uiid', 'created_at')
    
@admin.register(LessonComment)
class LessonCommentAdmin(admin.ModelAdmin):
    list_filter = ('id', 'user', 'lesson', 'comment', 'created_at')
    ordering = ('comment',)
    fields = ('id', 'user', 'lesson', 'comment', 'created_at')
    readonly_fields = ('id', 'created_at')
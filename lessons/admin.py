from django.contrib import admin
from .models import LessonTag, LessonCategory, Lesson
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
class LessonTagAdmin(admin.ModelAdmin):
    list_filter = ('uiid', 'tag', 'category', 'author', 'user', 'topic', 'created_at')
    ordering = ('topic',)
    fields = ('uiid', 'tag', 'category', 'author', 'user', 'topic', 'description', 'cash', 'payment')
    readonly_fields = ('uiid', 'created_at')
    
from django.contrib import admin
from .models import Order, OrderLesson
# # Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('uuid', 'user')
    ordering = ('user',)
    fields = ('uuid', 'user')
    readonly_fields = ('uuid',)
    
admin.site.register(OrderLesson) 
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils import timezone
# from lessons.models import Lesson
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Order(models.Model):
    uuid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    lessons = models.ManyToManyField('lessons.Lesson', through='OrderLesson')

    def update_total_price(self):
        with transaction.atomic():
            self.total_price = sum(op.cash for op in self.order_lessons.all())
            self.save()

    def __str__(self):
        return f"Замовлення {self.uuid} {self.user.username} {self.total_price}"

class OrderLesson(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_lessons')
    lesson = models.ForeignKey('lessons.Lesson', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)

    @property
    def cash(self):
        return self.lesson.cash * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.lesson.topic} (Замовлення {self.order.uuid})"

@receiver(post_save, sender=OrderLesson)
def update_order_total_price(sender, instance, **kwargs):
    instance.order.update_total_price()
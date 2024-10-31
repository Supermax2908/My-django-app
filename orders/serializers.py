from orders.models import Order, OrderLesson
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from lessons.serializers import LessonSerializer
from lessons.models import Lesson
from django.contrib.auth.models import User

class OrderLessonViewSerializer(ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = OrderLesson
        fields = ('lesson', 'quantity')


class OrderLessonSerializer(ModelSerializer):
    lesson = SlugRelatedField(slug_field='topic', queryset=Lesson.objects.all())
    class Meta:
        model = OrderLesson
        fields = ('lesson', 'quantity')

    def to_representation(self, instance):
        return OrderLessonViewSerializer().to_representation(instance)


class OrderSerializer(ModelSerializer):
    user = SlugRelatedField(slug_field='username', queryset=User.objects.all())
    order_lessons = OrderLessonSerializer(many=True)

    class Meta:
        model = Order
        fields = ('uuid', 'user', 'order_lessons', 'created_at')
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        order_lessons = validated_data.pop('order_lessons')
        order = Order.objects.create(**validated_data)

        for order_lesson in order_lessons:
            OrderLesson.objects.create(order=order, **order_lesson)
        return order
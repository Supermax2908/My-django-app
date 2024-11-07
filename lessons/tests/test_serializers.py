from django.test import TestCase

from lessons.models import Lesson
from lessons.serializers import LessonSerializer


class SerializersTestCase(TestCase):
    def test_lesson_serializer(self):
        lesson = Lesson.objects.create(topic='English language as the easiest language in the world', cash=50)
        serializer = LessonSerializer(lesson)

        self.assertEqual(serializer.data['display_name'], 'English language as the easiest language in the world')

    def test_lesson_serializer_cash(self):
        lesson = Lesson.objects.create(topic='English language as the easiest language in the world', price=99)
        serializer = LessonSerializer(lesson)

        self.assertEqual(serializer.data['display_name'], 'English language as the easiest language in the world 💰')
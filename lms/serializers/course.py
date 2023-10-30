from rest_framework import serializers

from lms.models import Course, Lesson
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'img_preview', 'description', 'lessons', 'lesson_count')

    @staticmethod
    def get_lesson_count(obj):
        return Lesson.objects.filter(course=obj).count()

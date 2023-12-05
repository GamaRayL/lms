from lms.models import Course, Lesson, Subscription
from rest_framework import serializers
from lms.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)
    is_user_subscribe = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'owner', 'img_preview', 'description', 'lessons', 'lesson_count', 'is_user_subscribe')

    @staticmethod
    def get_lesson_count(obj):
        return Lesson.objects.filter(course=obj).count()

    def get_is_user_subscribe(self, obj):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=obj, is_active=True).exists()


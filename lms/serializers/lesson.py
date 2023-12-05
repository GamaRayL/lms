from lms.models import Lesson
from rest_framework import serializers

from lms.validators.lesson import VideoUrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            VideoUrlValidator(field='video_url')
        ]

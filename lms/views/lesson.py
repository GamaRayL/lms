from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from lms.models import Lesson
from lms.paginations import LMSPagination
from lms.permissions import IsModerator, IsOwner, IsAdmin
from lms.serializers.lesson import LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsOwner | IsAdmin]
    pagination_class = LMSPagination

    def get_queryset(self):
        if IsModerator().has_permission(self.request, self) or IsAdmin().has_permission(self.request, self):
            queryset = Lesson.objects.all().order_by('id')
        else:
            queryset = Lesson.objects.filter(owner=self.request.user).order_by('id')

        return queryset.order_by('id')

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]

    def get_object(self):
        lesson = super().get_object()
        if lesson.owner != self.request.user:
            return Response({'error': 'У вас нет разрешения на доступ к этому уроку.'}, status=403)
        return lesson


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsModerator | IsAdmin]

    def create(self, request, *args, **kwargs):
        if IsModerator().has_permission(request, self):
            return Response({'error': 'У вас нет разрешения на создание уроков.'}, status=403)
        return super().create(request, *args, **kwargs)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator | IsOwner]

    def get_object(self):
        lesson = super().get_object()
        if lesson.owner != self.request.user:
            return Response({'error': 'У вас нет разрешения на обновление этого урока.'}, status=403)
        return lesson


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsModerator]

    def delete(self, request, *args, **kwargs):
        if IsModerator().has_permission(request, self):
            return Response({'error': 'У вас нет разрешения на удаление уроков.'}, status=403)
        return super().delete(request, *args, **kwargs)

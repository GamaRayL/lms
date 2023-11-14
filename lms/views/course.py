from lms.models import Course
from rest_framework import viewsets, status
from rest_framework.response import Response

from lms.paginations import LMSPagination
from lms.permissions import IsModerator, IsOwner, IsAdmin
from lms.serializers.course import CourseSerializer
from django.core.exceptions import PermissionDenied

from lms.services import subscriber_notice
from lms.tasks import notification_task


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator | IsOwner | IsAdmin]
    pagination_class = LMSPagination

    def list(self, request, *args, **kwargs):
        if IsOwner().has_permission(self.request, self):
            queryset = Course.objects.filter(owner=self.request.user).order_by('id')
        else:
            queryset = Course.objects.all().order_by('id')

        pagination_queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(pagination_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.role == 'moderator' or obj.owner == request.user:
            serializer = self.get_serializer(obj)
            return Response(serializer.data)
        raise PermissionDenied({'detail': 'У вас нет разрешения на доступ к этому уроку.'})

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if request.user.role == 'moderator' or obj.owner == request.user:
            serializer = self.get_serializer(obj, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            notification_task.delay(obj.id)

            return Response(serializer.data)
        return Response({'error': 'У вас нет разрешения на обновление этого урока.'}, status=403)

    def create(self, request, *args, **kwargs):
        if not IsModerator().has_permission(request, self):
            return Response({'error': 'У вас нет разрешения на создание уроков.'}, status=403)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        if IsModerator().has_permission(request, self):
            return Response({'error': 'У вас нет разрешения на удаление уроков.'}, status=403)



from lms.models import Course
from rest_framework import viewsets
from rest_framework.response import Response

from lms.paginations import LMSPagination
from lms.permissions import IsModerator, IsOwner
from lms.serializers.course import CourseSerializer
from django.core.exceptions import PermissionDenied


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsModerator | IsOwner]
    pagination_class = LMSPagination

    def list(self, request, *args, **kwargs):
        if IsModerator().has_permission(self.request, self):
            queryset = Course.objects.all().order_by('id')
        else:
            queryset = Course.objects.filter(owner=self.request.user).order_by('id')

        pagination_queryset = self.paginate_queryset(queryset)
        serializer = self.get_serializer(pagination_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != request.user:
            raise PermissionDenied({'detail': 'У вас нет разрешения на доступ к этому уроку.'})
        serializer = self.get_serializer(obj)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.owner != self.request.user:
            return Response({'error': 'У вас нет разрешения на обновление этого урока.'}, status=403)
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if IsModerator().has_permission(request, self):
            return Response({'error': 'У вас нет разрешения на создание уроков.'}, status=403)

    def destroy(self, request, *args, **kwargs):
        if IsModerator().has_permission(request, self):
            return Response({'error': 'У вас нет разрешения на удаление уроков.'}, status=403)



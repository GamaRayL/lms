from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from lms.models import Course
from lms.permissions import IsModerator, IsOwner
from lms.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsOwner]

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated(), IsModerator()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(),
                    IsModerator() or IsOwner()]
        return [IsAuthenticated(),
                IsModerator() or IsOwner()]

    def get_queryset(self):
        if IsModerator().has_permission(self.request, self):
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not IsModerator().has_permission(self.request, self) and instance.owner != self.request.user:
            raise PermissionDenied("У вас нет разрешения на редактирование этого курса.")


from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views.course import CourseViewSet
from lms.views.lesson import LessonListAPIView, LessonDetailAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('', LessonListAPIView.as_view(), name='lessons'),
    path('payments/', PaymentListView.as_view(), name='payments'),
    path('<int:pk>/', LessonDetailAPIView.as_view(), name='lesson'),
    path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
              ] + router.urls

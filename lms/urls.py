from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views.course import CourseViewSet
from lms.views.payment import PaymentListAPIView
from lms.views.lesson import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView, LessonRetrieveAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('payment/', PaymentListAPIView.as_view(), name='payments'),
    path('lesson/', LessonListAPIView.as_view(), name='lessons'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),
              ] + router.urls

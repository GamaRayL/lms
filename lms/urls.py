from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views.course import CourseViewSet
from lms.views.payment import PaymentListAPIView, PaymentCreateAPIView
from lms.views.lesson import LessonListAPIView, LessonCreateAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView, LessonRetrieveAPIView
from lms.views.subscription import SubscriptionViewSet

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = [
    # lessons
    path('lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),

    # payments
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
    path('payments/create', PaymentCreateAPIView.as_view(), name='payment_create'),
              ] + router.urls

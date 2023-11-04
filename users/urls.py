from django.urls import path

from users.apps import UsersConfig
from users.serializers import MyTokenObtainPairSerializer
from users.views import UserListAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='users'),
    path('token/', MyTokenObtainPairSerializer, name='token_obtain_pair'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update')
]
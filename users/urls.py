from django.urls import path

from .apps import UsersConfig
from .views import MyTokenObtainPairView, UserUpdateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user_list'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update')
]
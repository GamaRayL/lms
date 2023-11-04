from django.db import models
from constants import NULLABLE
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    """Модель представляет пользователя в системе"""
    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    is_active = models.BooleanField(default=True, verbose_name='активен')
    key = models.CharField(max_length=10, **NULLABLE, verbose_name='ключ')
    phone = models.CharField(max_length=50, **NULLABLE, verbose_name='телефон')
    city = models.CharField(max_length=50, **NULLABLE, verbose_name='город')
    avatar = models.ImageField(**NULLABLE, verbose_name='аватарка')
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER, verbose_name='роль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            ("toggle_is_active", "Активировать или деактивировать пользователя"),
        ]

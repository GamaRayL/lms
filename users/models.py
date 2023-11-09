from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.db import models
from constants import NULLABLE
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')
    ADMIN = 'admin', _('moderator')


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given username must be set")
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(
            self.model._meta.app_label, self.model._meta.object_name
        )
        email = GlobalUserModel.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        permissions = [
            ("toggle_is_active", "Активировать или деактивировать пользователя"),
        ]

from django.db import models

from constants import NULLABLE, PAYMENT_METHOD_CHOICES
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    img_preview = models.ImageField(**NULLABLE, verbose_name='превью картинка')
    description = models.TextField(verbose_name='описание')


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    img_preview = models.ImageField(**NULLABLE, verbose_name='превью картинка')
    video_url = models.CharField(max_length=255, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='курс', related_name='lessons')


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    payment_date = models.DateField(auto_now_add=True, verbose_name='дата оплаты')
    paid_course_or_lesson = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс или урок')
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='сумма оплаты')
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES, verbose_name='способ оплаты')

    def __str__(self):
        return f'Платеж #{self.pk} от {self.user} на сумму {self.payment_amount}'

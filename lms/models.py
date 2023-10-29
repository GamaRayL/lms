from django.db import models

from constants import NULLABLE


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    img_preview = models.ImageField(**NULLABLE, verbose_name='превью картинка')
    description = models.TextField(verbose_name='описание')


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    img_preview = models.ImageField(**NULLABLE, verbose_name='превью картинка')
    video_url = models.CharField(max_length=255, verbose_name='ссылка на видео')
    course = models.ForeignKey(Course, **NULLABLE, on_delete=models.CASCADE, verbose_name='курс')


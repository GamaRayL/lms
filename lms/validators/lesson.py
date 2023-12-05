from rest_framework.serializers import ValidationError


class VideoUrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        valid_words = ['youtube.com']

        tmp_val = dict(value).get(self.field).lower()

        for word in valid_words:
            if word not in tmp_val:
                raise ValidationError('Ссылка на сторонние ресурсы! Доступен только `youtube.com`')

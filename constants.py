NULLABLE = {'null': True, 'blank': True}

CASH = 'Наличные'
TRANSFER = 'Перевод на счет'

PAYMENT_METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    ]

EXPECTED_DATA = {
            "id": 1,
            "name": "New lesson",
            "description": "New lesson description",
            "img_preview": None,
            "video_url": "https://www.youtube.com/watch?v=nLRL_NcnK-4",
            "course": None,
            "owner": None
        }
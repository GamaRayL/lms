NULLABLE = {'null': True, 'blank': True}

CASH = 'Наличные'
TRANSFER = 'Перевод на счет'

PAYMENT_METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    ]

EXPECTED_CREATE_DATA = {
            "id": 2,
            "name": "New lesson",
            "description": "New lesson description",
            "img_preview": None,
            "video_url": "https://www.youtube.com/watch?v=nLRL_NcnK-4",
            "course": None,
            "owner": None
        }

EXPECTED_DATA = {
            "id": 1,
            "name": "New lesson",
            "description": "New lesson description",
            "img_preview": None,
            "video_url": "https://www.youtube.com/watch?v=nLRL_NcnK-4",
            "course": None,
            "owner": None
        }

UPDATED_EXPECTED_DATA = {
            "id": 1,
            "name": "Updated lesson",
            "description": "Updated lesson description",
            "img_preview": None,
            "video_url": "https://youtube.com/watch?v=nLRL_NcnK-5",
            "course": None,
            "owner": None
        }
NULLABLE = {'null': True, 'blank': True}

CASH = 'Наличные'
TRANSFER = 'Перевод на счет'
PAYMENT_METHOD_CHOICES = [
        (CASH, 'Наличные'),
        (TRANSFER, 'Перевод на счет'),
    ]
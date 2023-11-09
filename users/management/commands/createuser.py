from users.models import User, UserRoles
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Команда для создания суперпользователя"""

    def handle(self, *args, **options):
        try:
            email = input('Почта: ')
            password = input('Пароль: ')
            user = User.objects.create_user(
                email=email,
                password=password,
                role=UserRoles.MEMBER
            )

            self.stdout.write(self.style.SUCCESS('Пользователь создан успешно "%s"' % user.email))
        except KeyboardInterrupt:
            self.stdout.write(self.style.WARNING("\nПрограмма была прервана пользователем (Ctrl + C)"))

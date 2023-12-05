Репозиторий содержит необходимые файлы для создания образа Docker с проектом Django, используя PostgreSQL, Redis и Celery с помощью Docker Compose.

## Dockerfile
Файл `Dockerfile`настраивает окружение для проекта Django.
Он использует официальный образ Python 3, устанавливает зависимости
проекта из `requirements.txt`и копирует файлы проекта в контейнер.

## Docker Compose
Файл `docker-compose.yaml`определяет сервисы и их конфигурации. Он включает сервисы для Django-приложения, базы данных PostgreSQL, Redis, Celery worker и Celery beat.


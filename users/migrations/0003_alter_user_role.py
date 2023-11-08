# Generated by Django 4.2.7 on 2023-11-08 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('member', 'member'), ('moderator', 'moderator'), ('admin', 'moderator')], default='member', max_length=10, verbose_name='роль'),
        ),
    ]
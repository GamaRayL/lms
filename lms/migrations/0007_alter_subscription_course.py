# Generated by Django 4.2.7 on 2023-11-07 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0006_rename_subscribe_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='course',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='курс'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-03 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interior', '0003_alter_zayavka_user_z'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='time_z',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания'),
        ),
    ]

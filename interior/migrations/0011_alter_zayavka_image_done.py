# Generated by Django 3.2.21 on 2023-10-05 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interior', '0010_alter_zayavka_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='image_done',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
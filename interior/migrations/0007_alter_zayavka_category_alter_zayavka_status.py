# Generated by Django 4.2.5 on 2023-10-03 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interior', '0006_alter_zayavka_category_alter_zayavka_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interior.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='zayavka',
            name='status',
            field=models.CharField(blank=True, choices=[('new', 'Новая'), ('done', 'Выполнено'), ('accepted', 'Принято в работу')], default='new', help_text='Состояние заявки', max_length=10, null=True),
        ),
    ]

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from datetime import datetime
from django.core.exceptions import ValidationError


class User(AbstractUser):
    fio = models.CharField('ФИО', max_length=40, blank=True, null=True, validators=[
        RegexValidator(
            regex='^[а-яА-Я- ]*$',
            message=' только кириллические буквы, дефис и пробелы',
            code='invalid_username'
        ),
    ])
    accept = models.BooleanField('согласие на обработку персональных данных', default=True)

    class Meta(AbstractUser.Meta):
        pass


class Zayavka(models.Model):
    STATUS = (
        ('n', 'Новая'),
        ('s', 'Выполнено'),
        ('a', 'Принято в работу'),
    )
    user_z = models.ForeignKey(User,verbose_name="пользователь", on_delete=models.CASCADE)
    name_z = models.CharField('Название', max_length = 30 )
    desc_z = models.TextField('Описание', max_length = 300)
    status = models.CharField(max_length=1, choices=STATUS, default='n',blank=True,null=True, help_text='Состояние заявки')
    time_z = models.DateField("Время создания",blank=True,null=True,default=lambda: datetime.now())
    image = models.FileField(blank=True,null=True,)
    def __str__(self):
        return self.name_z

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator



class User(AbstractUser):
   fio = models.CharField('ФИО',max_length=40, blank=True,null=True,    validators=[
        RegexValidator(
            regex='^[а-яА-Я- ]*$',
            message=' только кириллические буквы, дефис и пробелы',
            code='invalid_username'
        ),
    ])
   accept = models.BooleanField('согласие на обработку персональных данных',default=True)


   class Meta(AbstractUser.Meta):
       pass
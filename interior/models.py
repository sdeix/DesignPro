from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from datetime import datetime
from django.core.exceptions import ValidationError
from django.urls import reverse

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

class Category(models.Model):
    name_category = models.CharField('Название', max_length = 30 )
    def __str__(self):
        return self.name_category
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('category_delete', args=[str(self.id)])

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')
        
class Zayavka(models.Model):
    STATUS = (
        ('new', 'Новая'),
        ('done', 'Выполнено'),
        ('accepted', 'Принято в работу'),
    )
   
    name_z = models.CharField('Название', max_length = 30 )
    desc_z = models.TextField('Описание', max_length = 300)
    category = models.ForeignKey(Category,verbose_name="Категория",on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='new',blank=True,null=True, help_text='Состояние заявки')
    time_z = models.DateTimeField(auto_now_add=True, editable=True,verbose_name="Время создания",blank=True,null=True, )
    image = models.FileField(validators=[file_size])
    user_z = models.ForeignKey(User,verbose_name="пользователь", on_delete=models.SET_NULL,null=True,blank=True)
    image_done = models.FileField("Выполненый дизайн",null=True,blank=True)
    comment = models.TextField('Комментарий', max_length=300,null=True,blank=True)
    def __str__(self):
        return self.name_z
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('deletez', args=[str(self.id)])
    def get_context(self):
        acc = Zayavka.objects.filter(status='accepted').count()
        return Zayavka.objects.filter(status='accepted').count()
    def set_accepted(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('accept', args=[str(self.id)])

    def set_done(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('done', args=[str(self.id)])

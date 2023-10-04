from django.contrib.auth.forms import UserCreationForm
from .models import User, Zayavka, Category
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ('fio', 'username', 'email','accept')

class CreationFormZ(forms.ModelForm):
    class Meta:
        model = Zayavka

        fields = ['name_z','category','desc_z','image','user_z']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = ['name_category']

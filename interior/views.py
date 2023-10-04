from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView


# Create your views here.
def index(request):
    return render(request, 'index.html')


class BBLoginView(LoginView):
    template_name = 'register/login.html'


class BBLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'register/logout.html'

    # users/views.py


# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm, CreationFormZ, CategoryForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('index')
    template_name = 'register/reg.html'


class CreateZ(CreateView):
    form_class = CreationFormZ
    success_url = reverse_lazy('index')
    template_name = 'createz.html'


from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Zayavka, Category
class AdminListZ(PermissionRequiredMixin, ListView):
    template_name = 'admin_list.html'
    model = Zayavka
    paginate_by = 0
    permission_required = 'catalog.can_markd'

class ListZ(LoginRequiredMixin, ListView):
    template_name = 'listz.html'
    model = Zayavka
    paginate_by = 10

    def get_queryset(self):
        return Zayavka.objects.filter(user_z=self.request.user).order_by('time_z')

class Index(ListView):
    template_name = 'index.html'
    model = Zayavka

    def get_queryset(self):
        return Zayavka.objects.filter(status="done").order_by('-time_z')[:4]


class CategoryList(PermissionRequiredMixin, ListView):
    template_name = 'category_list.html'
    model = Category
    paginate_by = 10
    permission_required = 'catalog.can_mark_returned'
class CategoryDelete(PermissionRequiredMixin, DeleteView):
    success_url = reverse_lazy('category_list')
    template_name = "category_confirm_delete.html"
    model = Category
    permission_required = 'catalog.can_mark_returned'
class CategoryCreate(PermissionRequiredMixin,CreateView):
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')
    template_name = 'category_create.html'
    permission_required = 'catalog.can_mark_returned'
class DeleteZ(LoginRequiredMixin, DeleteView):
    success_url = reverse_lazy('index')
    template_name = "zayavka_confirm_delete.html"
    model = Zayavka

class Done(UpdateView):
    model = Zayavka
    success_url = reverse_lazy('admin_list')
    template_name = 'done.html'
    fields = ['image_done','status']

class Accept(UpdateView):
    model = Zayavka
    success_url = reverse_lazy('admin_list')
    template_name = 'accept.html'
    fields = ['comment','status']

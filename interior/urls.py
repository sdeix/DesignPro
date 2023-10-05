from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from . import views
from .views import BBLoginView, BBLogoutView


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('reg/', views.SignUp.as_view(), name='reg'),
    url('createZ/', views.CreateZ.as_view(), name='createz'),
    url('category_create/', views.CategoryCreate.as_view(), name='category_create'),
    url('admin_list/', views.AdminListZ.as_view(), name='admin_list'),
    url('listZ/', views.ListZ.as_view(), name='listz'),
    url('category_list/', views.CategoryList.as_view(), name='category_list'),

    url(r'^delete/(?P<pk>\d+)$', views.DeleteZ.as_view(),name='deletez'),
    url(r'^accept/(?P<pk>\d+)$', views.Accept.as_view(),name='accept'),
    url(r'^done/(?P<pk>\d+)$', views.Done.as_view(),name='done'),
    url(r'^categorydelete/(?P<pk>\d+)$', views.CategoryDelete.as_view(),name='category_delete')

]


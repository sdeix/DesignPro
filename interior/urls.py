from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from . import views
from .views import BBLoginView, BBLogoutView


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', BBLoginView.as_view(), name='login'),
    path('logout/', BBLogoutView.as_view(), name='logout'),
    path('reg/', views.SignUp.as_view(), name='reg'),
    url('createZ/', views.CreateZ.as_view(), name='createz'),
    url('listZ/', views.ListZ.as_view(), name='listz'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteZ.as_view(),name='deletez')
]


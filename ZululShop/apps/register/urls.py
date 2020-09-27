from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    re_path(r'users/(?P<id>\w+)/', views.index, name='users'),
    re_path(r'myprofile/', views.myprofile, name='myprofile'),
]




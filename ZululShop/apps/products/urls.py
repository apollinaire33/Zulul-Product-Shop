from django.urls import path, include, re_path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'),
    re_path(r'search/', views.search, name='search'),
    re_path(r'adding/', views.AddView.as_view(), name='add'),
    re_path(r'productinfo/(?P<id>\w+)/', views.productinfo, name='productinfo'),
]
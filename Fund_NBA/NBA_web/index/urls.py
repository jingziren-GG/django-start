# -*- conding:utf-8 -*-
from django.urls import path
from . import views
from .views import IndexViews,EastViews,WestViews,FirstViews

app_name = 'index'
urlpatterns = [
    path('index/',IndexViews.as_view(),name='index'),
    path('east/',EastViews.as_view(),name='east'),
    path('west/',WestViews.as_view(),name='west'),
    path('homepage/',views.homepage,name='homepage'),
    path('<int:pk>/',FirstViews.as_view(),name='first'),
    path('',views.homepage,name='homepage'),
]
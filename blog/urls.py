# -*- coding:utf-8 -*-

__author__ = 'alex'
from django.conf.urls import url,include
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'index', IndexView.as_view(),name='index'),
]

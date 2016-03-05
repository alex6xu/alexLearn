# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.sessions.models import Session

# Create your views here.
class IndexView(View):
    def get(self,request):

        return render(request, 'blog/index.html')
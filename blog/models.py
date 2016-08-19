# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
# from myuser.models import *
# Create your models here.

class Essey(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64,blank=False)
    # author = models.ForeignKey(AuthUser,verbose_name='作者')
    #value = models.CharField(max_length=253)
    description = models.CharField(max_length=253, blank=True, null = True)
    content = models.TextField()
    createTime = models.DateTimeField('创建时间',blank=False,null=False)
    lastEdit = models.DateTimeField('修改时间',blank=False,null=False)
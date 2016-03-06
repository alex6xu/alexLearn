# -*- coding:utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.OneToOneField(User,unique=True,verbose_name=('用户名'))
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    #username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    mobile = models.CharField(max_length=11,blank=False,null=False)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    user_head = models.CharField(max_length=128,default='/static/admin/userHead/default.png')

    # class Meta:
    #     managed = True
    #     db_table = 'auth_user'

    # def __unicode__(self):
    #     return u'%s: %d ' % (self.user, self.id)
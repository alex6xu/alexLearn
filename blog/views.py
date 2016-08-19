# -*- coding:utf-8 -*-
from django.shortcuts import render,render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django import forms
from django.contrib.sessions.models import Session
from django.contrib import auth
from django.contrib.auth.models import User
import time
from django.template import RequestContext
# from myuser.models import *
from django import forms
from captcha.fields import CaptchaField


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20,label='name')
    email = forms.EmailField(max_length=64,label='email')
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm',widget=forms.PasswordInput)
    phone = forms.CharField(max_length=11,label='phone')
    checkcode = CaptchaField()



class LoginForm(forms.Form):
    username = forms.CharField(max_length=20,label='name')
    password = forms.CharField(widget=forms.PasswordInput)


# Create your views here.
class IndexView(View):
    def get(self,request):

        return render(request, 'blog/index.html')

class UserRegister(View):
    def get(self,requset):
        forms = RegisterForm()

        return render(requset,'blog/register.html',{'form':forms})

    def post(self,request):
        print 'post register start'
        curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        print 'request.user ', request.user

        if request.user.is_authenticated():#a*******************
            errors ='user authenticated !'
            print errors
            return HttpResponseRedirect("/blog/user/"+str(request.user))

        try:
            print 'get params'
            if request.method=='POST':
                print 'post method'
                username=request.POST.get('username','')
                print username
                password1=request.POST.get('password','')
                print password1
                password2=request.POST.get('password2','')
                print password2
                email=request.POST.get('email','')
                print email
                phone=request.POST.get('phone','')
                print phone
                errors=[]


                registerForm = RegisterForm(request.POST)#b********
                if not registerForm.is_valid():
                    errors.extend(registerForm.errors.values())
                    print 'register not valid'
                    return render_to_response("blog/userregister.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))
                else:
                    human = True
                if password1!=password2:
                    errors.append("两次输入的密码不一致!")
                    print 'pwd not same'
                    return render_to_response("register.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))

                filterResult = User.objects.filter(username=username)#c************
                if len(filterResult)>0:
                    errors.append("用户名已存在")

                    print 'user exist'
                    return render_to_response("blog/userregister.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))

                user=User.objects.create_user(username=username,password=password1,email=email)#d************************
                # user.username=username
                # user.set_password(password1)
                # user.email=email
                user.save()
                print 'saved user info to db'
                #用户扩展信息 profile
                # profile=AuthUser()#e*************************
                # profile.user_id=user.id
                # profile.phone=phone
                # profile.save()
                #登录前需要先验证
                newUser=auth.authenticate(username=username,password=password1)#f***************
                if newUser is not None:
                    auth.login(request, newUser)#g*******************
                    return HttpResponseRedirect("/blog/user/"+str(username))
        except Exception,e:
            print e
            errors.append(str(e))
            return render_to_response("register.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))

        return render_to_response("blog/index.html",RequestContext(request,{'curtime':curtime}))

        # jstr = {'result':1}
        # return HttpResponse(jstr)

def loginUser(request):
    if request.method is "GET":
        pass
        return render(request,'')

class LoginView(View):
    def get(self,request):
        form = LoginForm()

        return render(request,'blog/login.html' , {'form':form})

    def post(self,request):

        username = request.POST.get('username')
        password = request.POST.get('password')
        form = LoginForm(request.POST)
        if form.is_valid():
            # human = True
            user = auth.authenticate(username=username,password=password)
            # if user:
            #     auth.login(request,user)
        loginstatus = dict()
        try:
            user = auth.authenticate(username=username, password=password)
            #user = User.objects.filter(username=username)

            if(user is not None and user.is_active):
                auth.login(request,user)
                #if(user_pass):
                result = 1
                userid = user[0].id
                last_login = user[0].last_login
                is_superuser = user[0].is_superuser
                first_name = user[0].first_name
                last_name = user[0].last_name
                email = user[0].email
                loginstatus = {'res':result, 'id':userid,'username': username ,'last_login':last_login,'is_superuser':is_superuser
                          , 'first_name':first_name,'last_name':last_name,'email':email }
                return render(request,'blog/index.html',loginstatus)

            else:
                result = -1
                messg = 'auth failed'
                return render(request, 'blog/login.html')


        except Exception, e:
            print e
            return render(request,"blog/login.html")



class AboutMe(View):
    def get(self,request):

        return render(request,'blog/aboutme.html')

class ShowPageList(View):
    def get(self,request):

        return render(request,'')

    def post(self,request):

        return render(request,'')

class AddEssay(View):
    def get(self,request):

        return render(request,'blog/add.html')

    def post(self,request):

        jstr={'result' : 'ok'}
        return HttpResponse(jstr)
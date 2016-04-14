from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from django import forms
from django.core.mail import send_mail

import uuid
import time
import json

# from .models import User
# from .form import UserRegisterForm
# from .form import UserLoginForm
from .models import *
from .form import *

#发送验证码到邮箱
def send_active_code(active_code, email):
	send_mail('验证码', active_code, '524360108@qq.com', [email, ])

#生成验证码
def gen_active_code(email):
    return uuid.uuid5(uuid.NAMESPACE_DNS, email+str(time.time())).hex[15:21]

#检查是否登录
def check_login(f):
	def wrapped_f(req):
		email = req.session.get('email', None)
		if not email:
			rs = {'success': False, 'msg': '请先登录！'}
			return JsonResponse(rs)
		else:
			user = User.objects.filter(email__exact=email)
			if not user:
				rs = {'success': False, 'msg': '登录的用户不存在！请重新登录！'}
				return JsonResponse(rs)
		return f(req)
	return wrapped_f

#检查是否未登录
def check_unlogin(f):
	def wrapped_f(req):
		email = req.session.get('email', None)
		if email:
			rs = {'success': False, 'msg': '已登录！请先登出！'}
			return JsonResponse(rs)
		return f(req)
	return wrapped_f

#注册
@check_unlogin
def register(req):
	if req.method == 'POST':
		uf = UserRegisterForm(req.POST)
		if uf.is_valid():
			#获得表单数据
			email = uf.cleaned_data['email']
			password = uf.cleaned_data['password']
			name = uf.cleaned_data['name']

			active_code = gen_active_code(email)
			#添加到数据库
			send_active_code(active_code, email)
			User.objects.create(email=email, password=password, name=name, active_code=active_code)

			req.session['email'] = email
			rs = {'success': True, 'msg': '注册成功！账户未激活！'}

		else:
			rs = {'success': False, 'msg': uf.errors}
		return JsonResponse(rs)
	else:
		uf = UserRegisterForm()
	return render_to_response('register.html', {'uf':uf}, context_instance=RequestContext(req))

#登陆
@check_unlogin
def login(req):
	if req.method == 'POST':
		uf = UserLoginForm(req.POST)
		if uf.is_valid():
			#获取表单用户密码
			email = uf.cleaned_data['email']
			password = uf.cleaned_data['password']
			#获取的表单数据与数据库进行比较
			user = User.objects.filter(email__exact=email, password__exact=password)
			if user:
				#登录成功
				rs = {'success': True, 'msg': '登录成功！', }
				req.session['email'] = email
			else:
				#登录失败
				rs = {'success': False, 'msg': '用户名或密码不正确！'}
		else:
			rs = {'success': False, 'msg': uf.errors}
		return JsonResponse(rs)
	else:
		uf = UserLoginForm()
	return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))

#发送验证码
@check_login
def send_code(req):
	email = req.session['email']
	user = User.objects.get(email=email)

	active_code = gen_active_code(email)
	#添加到数据库
	send_active_code(active_code, email)
	user.active_code = active_code
	user.save()

	rs = {'success': True, 'msg': '验证码已发送！'}
	return JsonResponse(rs)

#激活账户
@check_login
def active(req):
	email = req.session['email']
	user = User.objects.get(email=email)

	active_code_in = req.POST['active_code'].lower() if req.POST.has_key('active_code') else None

	if user.active_code==active_code_in:
		user.is_active = True
		user.save()

		rs = {'success': True, 'msg': '账户激活成功！'}
	else:
		rs = {'success': True, 'msg': '验证码错误！'}
	return JsonResponse(rs)

#主页面
def index(req):
	email = req.session.get('email', None)
	return render_to_response('index.html' ,{'username': email})

#退出
@check_login
def logout(req):
	rs = {'success': True, 'msg': '登出成功！', }
	del req.session['email']
	return JsonResponse(rs)

#上传图片并返回图片地址
def upload(request):
    if request.method == "POST":
        uf = UserForm(request.POST,request.FILES)
        if uf.is_valid():
            # username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            test=Test()
            # test.username=username
            test.headImg=headImg
            test.save()
            rs={'success': True, 'msg': '上传成功！','mapurl':json.dumps(str(test.headImg))}
			# rs=json.dump(rs)
        else:
            rs = {'success': True, 'msg': '上传失败！'}
            # return HttpResponse('upload ok!')
        return JsonResponse(rs)
    else:
        uf = UserForm()
    return render_to_response('upload.html',{'uf':uf})

#获取比赛地图列表
from django.core import serializers
def matchlist(request):
    if request.method == "POST":
        uf = matchlistForm(request.POST)
        if uf.is_valid():
            num = uf.cleaned_data['num']
            json_data = serializers.serialize("json",Match.objects.all().order_by("-uploadtime")[5*num:5*(num+1)-1:1])
        return HttpResponse(json_data, content_type="application/json")
    else:
        uf = matchlistForm()
    return render_to_response('matchlist.html', {'uf': uf}, context_instance=RequestContext(request))

#获取房间列表
def roomlist(request):
    if request.method == "POST":
        uf = roomlistForm(request.POST)
        if uf.is_valid():
            num = uf.cleaned_data['num']
            json_data = serializers.serialize("json", Room.objects.all().order_by("-createtime")[5 * num:5 * (num + 1) - 1:1])
        return HttpResponse(json_data, content_type="application/json")
    else:
        uf = roomlistForm()
    return render_to_response('roomlist.html', {'uf': uf}, context_instance=RequestContext(request))
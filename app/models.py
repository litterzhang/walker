from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator, MinLengthValidator

# Create your models here.

#应用主要逻辑和功能
#1.用户可以注册与登录
#2.用户可以创建比赛地图，公开/私有，私有只能自己看到。
#3.用户可以选择公开/私有地图创建房间，房间设置邀请码，这个是所有用户都能看到的。
#4.用户可以进入房间，开始比赛。
#说明：每一个比赛地图，由若干个含有地点信息的图片组成，称之为“标记点”，即1个比赛地图包含n个标记点，参赛者需要根据标记点拍摄相同照片。
#每个表的primary key为id，django默认自增，不用再写了。
#用户表
class User(models.Model):
	email = models.CharField(max_length=200, unique=True, validators=[EmailValidator(message='邮箱格式不正确！'), ])
	name = models.CharField(max_length=50, default='越野用户', blank=True)
	sex = models.CharField(max_length=2, blank=True)
	age = models.IntegerField(default=0, blank=True)
	password = models.CharField(max_length=20, validators=[MinLengthValidator(8, message='密码长度在8-20之间'), ])
	#头像
	avatar = models.CharField(max_length=200, blank=True)
	#签名
	signature = models.CharField(max_length=200, blank=True, default='这个人很懒，什么都没有留下')
	is_active = models.BooleanField(default=False)
	active_code = models.CharField(max_length=40, blank=True)

#比赛地图表
class Match(models.Model):
	name = models.CharField(max_length=50, default="比赛地图", editable=False)
	#封面（宣传图）
	cover = models.CharField(max_length=200, default='xxx.jpg', editable=False)
	#比赛地图创建者id，关联User表查询更多信息
	creatorid = models.IntegerField()
	#是否公开
	ispubic = models.BooleanField()
	place = models.CharField(max_length=50, default="比赛地点", editable=False)
	#上传时间
	uploadtime = models.TimeField(default=timezone.now())

#比赛标记点
class Marker(models.Model):
	#比赛地图id，关联User表查询更多信息
	match = models.ForeignKey(Match)
	#标记点图片
	marker = models.CharField(max_length=200, default='xxx.jpg', editable=False)
	#标记点顺序
	order = models.IntegerField()
	#经纬度
	lon = models.FloatField()
	lot = models.FloatField()
	

#比赛房间表（选择比赛地图后创建房间）
class Room(models.Model):
	name = models.CharField(max_length=50, default="比赛房间", editable=False)
	#比赛地图id,关联比赛地图表查询更多信息
	match = models.ForeignKey(Match)
	#比赛房间创建者id,关联Room表查询更多信息
	creatorid= models.IntegerField()
	creatorname = models.CharField()
	#邀请码
	code = models.IntegerField()
	start = models.DateTimeField()
	end = models.DateTimeField()
	detail = models.CharField(max_length=200, default='暂无详情', editable=False)

#比赛房间-用户-关联表
class Room_User(models.Model):
	#比赛房间id
	room = models.ForeignKey(Room)
	#参赛用户id
	user = models.IntegerField(User)
	#参赛用户成绩
	score = models.IntegerField()
	#比赛完成时间
	start = models.DateTimeField()
	end = models.DateTimeField()
	#是否中途退出
	isquit = models.BooleanField()

#比赛房间-用户-标记点关联表
class Room_User_Marker(models.Model):
	#比赛房间id
	room_user = models.ForeignKey(Room_User)
	#标记点图片
	marker = models.CharField(max_length=200, default='xxx.jpg', editable=False)
	#经纬度
	lon = models.FloatField()
	lot = models.FloatField()
	#图片上传时间
	uptime = models.DateTimeField()

import os
import time
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (instance.username, time.time(), ext)
    mydir ='./app/static/' + "%s" % instance.username
    return os.path.join(mydir, filename)

#测试的数据库表
class Test(models.Model):
    username = models.CharField(max_length = 30)
    headImg = models.FileField(upload_to = content_file_name)

    def __unicode__(self):
        return self.username












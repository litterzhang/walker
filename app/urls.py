from django.conf.urls import patterns, url
from app import views

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^send_code/$', views.send_code, name='send_code'),
	url(r'^active/$', views.active, name='active'),
	url(r'^index/$', views.index, name='index'),
	url(r'^match_new/$', views.match_new, name='match_new'),
	url(r'^upload/$', views.upload, name='upload'),
	url(r'^match_list/$', views.match_list, name='match_list'),
	url(r'^room_list/$', views.room_list, name='room_list'),
	url(r'^room_new/$', views.room_new, name='room_new'),
	url(r'^room_join/$', views.room_join, name='room_join'),
	url(r'^room_joined/$', views.room_joined, name='room_joined'),
]
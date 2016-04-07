from django.conf.urls import patterns, url
from app import views

urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^send_code/$', views.send_code, name='send_code'),
	url(r'^active/$', views.active, name='active'),
	url(r'^index/$', views.index, name='index'),
]
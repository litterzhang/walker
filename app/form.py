from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator, MinLengthValidator

from .models import User, Room

class UserRegisterForm(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password', 'name']

		labels = {
			'email': _('邮箱')
		}

		error_messages = {
			'email': {
				'unique': _('邮箱已被注册！')
			}
		}

class UserLoginForm(forms.Form):
	email = forms.CharField(max_length=200, validators=[EmailValidator(message='邮箱格式不正确！'), ])
	password = forms.CharField(max_length=20, validators=[MinLengthValidator(8, message='密码长度在8-20之间'), ])

class MatchNewForm(forms.Form):
	name = forms.CharField(max_length=50, initial='比赛地图', required=False)
	cover = forms.CharField(max_length=200, initial='xxx.jpg', required=False)
	ispublic = forms.BooleanField(required=True)
	place = forms.CharField(max_length=50, initial='比赛地点', required=False)
	json = forms.CharField(max_length=1000, initial='{}', required=False)

class UserForm(forms.Form):
    headImg = forms.FileField()

class MatchListForm(forms.Form):
	num = forms.IntegerField(required=False)
	me = forms.BooleanField(required=False)

class RoomListForm(forms.Form):
	num = forms.IntegerField(required=False)
	me = forms.BooleanField(required=False)

class RoomNewForm(ModelForm):
	class Meta:
		model = Room
		fields = ['name', 'match', 'start', 'end', 'code', 'detail']

		error_messages = {
			'match': {
				'required': _('邮箱已被注册！')
			}
		}

class RoomJoinForm(forms.Form):
	code = forms.IntegerField()
	room = forms.IntegerField()

	def clean(self):
		cleaned_data = super(RoomJoinForm, self).clean()
		code_d = cleaned_data.get('code', -1)
		room_id = cleaned_data.get('room', None)

		if not room_id or not len(Room.objects.filter(id=room_id)):
			self._errors['room'] = self.error_class([u'加入的房间不存在'])
		else:
			room_g = Room.objects.get(id=room_id)

			if room_g.code!=code_d:
				self._errors['code'] = self.error_class([u'邀请码不正确'])
			else:
				return cleaned_data



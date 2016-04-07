from django.forms import ModelForm
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import EmailValidator, MinLengthValidator

from .models import User

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

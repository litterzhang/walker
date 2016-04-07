# 定向越野API文档

### 注册
	HTTP POST
	地址：
	/app/register
	说明：	
	cookies中不可以有email，否则视为已登录，无法注册
	注册成功会发送激活码到注册邮箱，账户未激活
	参数：
	email : 注册邮箱，可能错误信息："邮箱格式不正确！"、"邮箱已被注册"
	password: 注册密码，可能错误信息："密码长度必须在8-20位之间"
	返回：
	{'success': True/False, 'msg':'信息'}

### 登录
	HTTP POST
	地址：
	/app/login
	说明：	
	cookies中不可以有email，否则视为已登录，无法登录
	参数：
	email : 注册时使用邮箱，可能错误信息："邮箱格式不正确！"
	password: 注册密码，可能错误信息："密码长度必须在8-20位之间"
	返回：
	{'success': True/False, 'msg':'登录成功！/用户名或密码不正确！'}
	登录成功需要记录cookies，用作之后的请求！

### 登出
	HTTP POST/GET
	地址：
	/app/logout
	说明：
	cookies中包含email，否则为未登录，无法登出
	参数：
	无
	返回：
	{'success': True/False, 'msg':'登出成功！/未登录'}

### 发送激活码
	HTTP POST
	地址：
	/app/send_code
	说明：
	cookies中包含email，否则为未登录，无法发送
	参数：
	无
	返回：
	{'success': True/False, 'msg':'验证码已发送！/未登录'}


### 激活账户
	HTTP POST
	地址：
	/app/active
	说明：
	cookies中包含email，否则为未登录，无法激活账户
	参数：
	active_code: 输入验证码
	返回：
	{'success': True/False, 'msg':'激活成功！/激活失败！'}
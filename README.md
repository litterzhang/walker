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
	

### 上传图片
	HTTP POST
	地址：
	/app/upload
	说明：
	传到服务器的参数中包含地图的信息
	返回：
	{'success': True/False, 'msg':'上传成功！/上传失败！','mapurl':'图片地址'}

### 上传比赛地图
	HTTP POST
	地址：
	/app/match_new
	说明:
	cookies中包含email，否则为未登录，无法创建比赛
	参数：
	name: 比赛名称
	cover: 比赛封面图, url
	ispublic: 是否公开
	place: 比赛地点
	返回：
	{'success': True/False, 'msg':'上传成功！/上传失败！'}
	
### 比赛地图列表
	HTTP POST
	地址：
	/app/matchlist
	参数：
	num: 0代表返回前5个，1代表返回第5到9个，2代表返回10到14个
	返回：
	{name,cover,creatorid,ispubic,place,uploadtime  这些都是json里的参数}
	
### 比赛房间列表
	HTTP POST
	地址：
	/app/roomlist
	参数：
	num: 0代表返回前5个，1代表返回第5到9个，2代表返回10到14个
	返回：
	{name,match,creatorid,creatorname,createtime,code,start,end,detail 这些都是json里的参数}

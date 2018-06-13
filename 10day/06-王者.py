print("欢迎来到王者荣耀")
i = 0
while i < 3:
	acc = int(input("请输入账号"))
	paw = int(input("请输入密码"))
	if acc == 123  and paw == 123456:
		print("登陆成功")
		xuan = int(input("选择你要的英雄范围"))
		if xuan == 0:
			print("鲁班大师")
		elif xuan == 1:
			print("程咬金")
		elif xuan == 3:
			print("王昭君")

	else:
		print("登录失败")
		i+=1	

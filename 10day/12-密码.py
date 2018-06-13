acc = 123
paw = 456
a = int(input("请输入用户名"))
b = int (input("请输入密码"))
if a == acc and b == paw:
	print("欢迎来到神秘世界")
elif a == acc and b != paw:
	print("密码错误")
elif a != acc and b == paw:
	print("账号错误")
else:
	print("密码和账号都有误")

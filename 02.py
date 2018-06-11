import random
i = 0
shu = random(1,100)
while i < 10 :
	cai =int(input("请输入数字1,100"))
	if cai > shu:
		print("过大")
	elif cai < shu:
		print("过小")
	else:
		print("猜对了")
	i+=1

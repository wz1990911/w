import random
a = random.randint(1,100)
i = 0
while i < 100:
	py = int(input("输入数值"))
	if py > a:
		print("过大了")
	elif py < a:
		print("过小了")
	else:
		print("猜对了")
		i = 100
	i+=1

import random
a = random.randint(1,100)
i = 0
while i < 10:
	b = int(input("输入数字"))
	if b > a:
		print("过大")
	elif b < a:
		print("过小")
	else:
		print("猜对了")
		i=10
	i+=1

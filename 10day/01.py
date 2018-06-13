'''
1 = 石头
2 = 剪刀
3 = 布
'''
import random
dan = random.randint(1,3)
ren = int(input("请输入1:石头 2:剪刀 3:布"))
if dan <= 3 and  ren > 0:
	if (ren == 1 and dan ==2) or (ren == 2 and dan == 2) or (ren == 3 and dan ==1):
		print("你赢了")
	elif ren == dan:
		print("平局")
	else:
		print("你输了")
else:
	print("输入不合法")

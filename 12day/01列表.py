l = ["laowang","laozhao","laogao","laozhao"]
n = input("输入你要查询的名字")
count = 0
for i in l:
	if n == i:
		print("找到了索引是%d"%count)
	count += 1




for p,i in enumerate(l):
	if n == i:
		print(p,i)

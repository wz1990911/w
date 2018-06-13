count = int(input("请输入一个数字"))
eve = 0
odd = 0
a = 0
x = 0
while x < count:
	print("当数字：%d"%x)
	x+=1
	if x%2 ==0:
		eve = eve + x
	elif x %2 !=0:
		odd = odd + x
print("偶数和为:%d"%eve)
print("奇数的和为:%d"%odd)
print("总和为:%d"%(eve+odd))

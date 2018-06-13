b = int(input("输入数字"))
a = 0
o_he = 0
j_he = 0
while a <= b:
	#print(a)
	if a % 2 == 0:
		print("偶数是%d"%a)
		o_he = o_he + a
	else:
		print("奇数是%d"%a)
		j_he = j_he + a
	a+=1
print("奇数的和是%d"%o_he)
print("偶数的和是%d"%j_he)
print("奇数和偶数的和是%d"%(o_he+j_he))

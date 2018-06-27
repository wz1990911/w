print("学生管理系统")
print("***********************正在进人*********************")
print("进入成功")
list1 = []
while True:
	tian = int(input("请选择功能:\n1----添加\n2----删除\n3----修改\n4----查找\n0----退出系统"))
	if tian == 1:
		name = input("请输入姓名")
		list1.append(name)
		print("添加成功")
		print(list1)
	elif tian == 2 :
		mz = input("请选择你要删除的姓名")
		if mz in list1:
			list1.remove(mz)
			print("已删除名字")
			print(list1)
		else:
			print("查无此人")
	elif tian == 3:
		gai = input("请输入要修改的名字")
		if gai in list1:
			xin = input("请输入新的名字")
			m = list1.index(gai)
			list1[m]=xin
			print("修改成功")
			print(list1)
	elif tian == 4:
		cha = input("请输入要查找的内容")
		if cha in list1:
			o = index(cha)
			print("你要查找找的人的索引是%d"%o)
		else:
			print("查无此人")
	elif tian == 0:
		print("退出成功")
		break
	else:	
		print("输入有误")

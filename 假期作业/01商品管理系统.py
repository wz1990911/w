print("欢迎来到商店管理系统")
print("*******************正在进入中*******************")
list1 = []
while True:
	a = int(input("请输入您的选择:\n1------新增商品\n2------删除商品\n3------修改商品\n4------查询商品\n0------退出系统"))
	if a == 1:
		list2 = []
		shang = input("请输入商品的名字")
		list2.append(shang)
		jia = float(input("请输入商品的价格"))
		list2.append(jia)
		list1.append(list2)
		print(list1)
		print("添加成功")
	elif a == 2:
		shan = input("请输入您要删除的商品")
		for position,i in enumerate(list1):
			if shan == i[0]:
				list1.pop(position)
				print(list1)
				print("删除成功")
	elif a == 3:
		name = input("请输入你要修改的商品")
		for i in list1:
			if a == i:
				print("1------修改名字")
				print("2------修改价格")
				print("3------修改名字和价格")
				nu = int(input("请选择"))
				if nu == 1:
					name = input("请输入新名字")
					i[0] = name
				elif nu == 2:
					price = float(input("请输入新价格"))
					i[1] = price
				elif nu == 3:
					name = input("请输入新名字")
					price = float(input("请输入新价格"))
					i[0] = name
					i[1] = price
					print(list1)
			

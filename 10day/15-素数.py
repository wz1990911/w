for i in range(2,101):
	flag = 0#假设2-101之间全素数
	for j in range(2,i):
		if i%j == 0:
			flag = 1
			break
	if flag == 0:
		print(i) 
		

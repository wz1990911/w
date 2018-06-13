i = 1
while i < 10:
	j = 1
	while j < i+1:
		c = i*j
		print("%d*%d=%d"%(j,i,c) , end = " \t")
		j+=1
	print("")
	i+=1

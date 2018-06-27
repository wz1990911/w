list = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":123331,"renkou":123123}}]
"""
for i in list:
	print(i)
	for d in i.keys():
		print(d)
	for a in i.values():
		print(a)
		for b in a.items():
			print(b)
			for c in b:
				print(c)
"""
for i in list:
	print(i)
	for a,b in i.items():
		#print(a,b)
		for c,d in b.items():
		#	print(c,d)
			print(a,c,d)

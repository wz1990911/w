id_card = {"name":"王哲","brithday":"1999.9.11","address":"地球村","end":"汉族","sex":"男"}
print(id_card)
print(type(id_card))
id_card["name"] = "laosong"
print(id_card)
id_card.setdefault("idnumber",142702199909112413)
id_card.setdefault("address","中国")
print(id_card)
id_card.popitem()
print(id_card)
del id_card["end"]
print(id_card)
for i in id_card:
	for j in id_card:
		print(j)

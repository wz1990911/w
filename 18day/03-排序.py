list = [10,16,45,80,45,63,82,12,48,88,100,90]
for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print(list)

list = [1,100,49,10,56,3,2,37]
i=0
while i<len(list):
    if list[i] == 3:
        print("索引是%d"%i)
        break
    i+=1
position = list.index(3)
print("索引是%d"%position)
list1 = [1,2,3,4,5,6,7,8,9]
min = 0
max = len(list1)-1
count = 3
while True:
    center=int((min+max)/2)
    if list1[center] > count:
        max = max-1
    elif list1[center] < count:
        max = max+1
    elif list1[center] == count:
        print("索引是%d"%center)
        break
for p,i in enumerate(list):
    if i == 3:
        print("索引是%d"%p)

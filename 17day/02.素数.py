list1 = []
def sushu():
    for i in range(2,201):
        flag = 0
        for j in range(2,i):
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            list1.append(i)
    return list1
res = sushu()
print(res)

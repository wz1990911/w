list1 = []
def su():
    for i in range(100,201):
        for j in range(2,i):
            flag = 0
            if i%j == 0:
                flag = 1
                break
        if flag == 0:
            list1
su() 


def nian(a):
    if a%400 ==0 or (a%4 == 0 and a%100 !=0):
        print("%d是闰年"%a)
    else:
        print("%d是平年"%a)
a = int(input("请输入年份"))
nian(a)

















list1 = []
#退出系统
def print_0():
    pass
#娱乐模式
def print_6():
    pass
#打印名片
def print_5():
    print("姓名\t+职业\t电话")
    for position,i in enumerate(list1):
        print(i["name"],i["zhi"],i["hao"])
#查找名片
def print_4():
    name = input("请输入要查找的名片")
    flag = 0
    for position,i in enumerate(list1):
        if name == i["name"]:
            flag = 1
            print("名字:%s\n职业:%s\n电话:%d"%(i["name"],i["zhi"],i["hao"]))
    if flag == 0:
        print("查无此人")
        
#修改名片
def print_3():
    name = input("请输入要修改的名片")
    flag = 0
    for position,i in enumerate(list1):
        if name == i["name"]:
            flag = 1
            print("1:修改名字")
            print("2:修改职位")
            print("3:修改号码")
            a = int(input("请输入序号"))
            if a == 1:
                i["name"] = input("请输入新名字")
                print("修改成功")
                print("list1")
            elif a == 2:
                i["zhi"] = input("请输入新职位")
                print("修改成功")
                print("list1")
            elif a == 3:
                i["hao"] = input("请输入新号码")
                print("修改成功")
                print(list1)
    if flag == 0:
        print("查无此人")
#删除名片O
def print_2():
    name = input("请输入要删除的名字")
    flag = 0
    for position,i in enumerate(list1):
        if name == i["name"]:
            flag = 1
            print("1:确认删除")
            print("2:取消删除")
            nu = int(input("请选择序号"))
            if nu == 1:
                list1.pop(position)
                print("删除成功")
                break
    if flag == 0:
        print("查无此人")
#添加名片
def print_1():
    name = input("请输入名字")
    zhi = input("请输入职位")
    hao = int(input("请输入手机号"))
    zi = {}
    zi["name"] = name
    zi["zhi"] = zhi
    zi["hao"] = hao
    list1.append(zi)
    print(list1)
    print("添加成功")



def print_ming():
    print("1------添加名片")
    print("2------删除名片")
    print("3------修改名片")
    print("4------查找名片")
    print("5------打印名片")
    print("6------娱乐模式")
    print("0------退出系统")
def print_diao():
    print("欢迎来到名片管理系统".center(50,"*"))
    while True:
        print_ming()
        a = int(input("请输入您的选择"))
        if a== 1:
            print_1()
        elif a == 2:
            print_2()
        elif a == 3:
            print_3()
        elif a == 4:
            print_4()
        elif a == 5:
            print_5()
        elif a == 6:
            print_6()
        elif a == 0:
            print_0()
print_diao()

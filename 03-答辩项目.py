list1 = []
import random
import time
def print_name():
    time.sleep(1)
    print("1------添加参与活动的人名")
    print("2------删除不想参加的人名")
    print("3------打印人员名单")
    print("4------查找人名")
    print("5------修改人名")
    print("6------娱乐模式")
    print("0------退出系统")
def print_diao():
    time.sleep(1)
    print("欢迎来到节日娱乐系统".center(50,"*"))
    time.sleep(1)
    print("正在进入...")
    time.sleep(1)
    print("正在进入..")
    time.sleep(1)
    print("正在进入.")
    print("进入成功")
    while True:
        print_name()
        a = input("请输入选择")
        if a.isdigit():
            a = int(a)
        else:
            print("输入有误")
        if a == 1:
            time.sleep(1)
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
            print("已退出系统")
            break
#添加名字
def print_1():
    zi = {}
    while True:
        name = input("请输入名字")
        if len(name)>4:
            print("输入的名字不合法")
            continue
        else:
            break
    while True:
        sex = input("请输入性别")
        if sex == "男"or sex == "女":
            break
        else:
            print("输入不合法")
            continue
            break
    while True:
        age = input("请输入年龄")
        if len(age)<4 and age.isdigit():
            age = int(age)
            break
        else:
            print("输入不合法")
            continue
    while True:
        number = input("请输入联系方式")
        if len(number) != 11 or number.startswith("1") == False:
            print("输入有误")
            continue
        else:
            break
    zi["name"] = name
    zi["sex"] = sex
    zi["age"] = age
    zi["number"] = number
    list1.append(zi)
    print(list1)
    print("添加成功")

#删除名字
def print_2():
    name = input("请输入你要删除的名字")
    flag = 0#假设这里面没有你要的名字
    for position,i in enumerate(list1):
        if name == i["name"]:
            flag = 1
            print("1------确认删除")
            print("2------取消删除")
            select = int(input("请选择序号"))
            if select == 1:
                list1.pop(position)
                print("删除成功")
                print(list1)
            break
    if flag == 0:
        print("没有此人")
#打印名字
def print_3():
    print("姓名\t年龄\t性别\t  联系方式")
    for position,i in enumerate(list1):
        print(i["name"],"\t",i["age"],"\t",i["sex"],"\t",i["number"])
#查找名字
def print_4():
    name = input("请输入你要查找的名字")
    flag = 0
    for position,i in enumerate(list1):
        if name == i["name"]:
            flag = 1
            print("名字是:%s\n年龄是:%d\n性别是:%s\n电话是%d"%(i["name"],int(i["age"]),i["sex"],int(i["number"])))
            break
    if flag == 0:
        print("查无此人")
#修改名字
def print_5():
    name = input("请输入你要修改的名字")
    for position,i in enumerate(list1):
        flag = 0
        if name == i["name"]:
            flag = 1
            print("1------修改名字")
            print("2------修改年龄")
def print_4():
    name = input("请输入你要查找的名字")
    flag = 0
    for position,i in enumerate(list1):
        if name == i["name"]:
            flag = 1
            print("名字是:%s\n年龄是:%d\n性别是:%s\n电话是%d"%(i["name"],int(i["age"]),i["sex"],int(i["number"])))
            break
    if flag == 0:
        print("查无此人")
#修改名字
def print_5():
    name = input("请输入你要修改的名字")
    for position,i in enumerate(list1):
        flag = 0
        if name == i["name"]:
            flag = 1
            print("1------修改名字")
            print("2------修改年龄")
            print("3------修改性别")
            print("4------修改电话")
            print("0------退出修改")
            a = int(input("请选择序号"))
            if a == 1:
                i["name"] = input("输入新名字")
                print("修改成功")
            elif a ==2:
                i["age"] = input("输入新年龄")
                print("修改成功")
            elif a == 3:
                i["sex"] = input("输入性别")
                print("修改成功")
            elif a == 4:
                i["number"] = input("输入新手机号")
                print("修改成功")
            elif a == 0:
                break
    if flag == 0:
       print("查无此人")
#娱乐模式
def print_6():
    print("1------猜拳")
    print("2-------猜数字")
    a = input("请选择序号")
    if a.isdigit():
        a = int(a)
    else:
        print("输入错误")
    if a == 1:
        while True:
            time.sleep(1)
            b = random.randint(1,3)
            print("1------石头")
            print("2------剪刀")
            print("3------布")
            print("0------退出游戏")
            xuan = input("请选择")
            if xuan.isdigit():
                xuan = int(xuan)
            else:
                print("输入错误")
            if xuan >= 0 and xuan < 4:
                if xuan == 0:
                    break
                if (xuan == 1 and b == 2) or (xuan == 2 and b == 3)or (xuan == 3 and b == 1):
                    time.sleep(1)
                    print("你赢了")
                elif xuan == b:
                    time.sleep(1)
                    print("平局")
                elif xuan == 0:
                    break
print_diao()

list1 = []
list2 = []
list3 = []
list4 = []
import random
import time
def cuang():
    zi = {}
    print("欢迎来到荒岛体验系统".center(50,"*"))
    while True:
        print("账号等于11位并且都是纯数字才可以哦")
        acc = input("请注册账号")
        if len(acc) == 11 and acc.startswith("1"):
            break
        else:
            print("输入有误")
            continue
    while True:
        print("密码必须6位以上哦")
        pwd = input("请输入密码")
        if len(pwd)> 6:
            break
        else:
            print("输入有误")
            continue
    if len(acc) == 11 and acc.startswith("1") and len(pwd)> 6:
        print("注册成功")
        zi["acc"] = acc
        zi["pwd"] = pwd
        list1.append(zi)
        deng()
def deng():
    print("正在登录".center(50,"*"))
    print("正在进入.....")
    print("正在进入....")
    print("正在进入...")
    print("正在进入..")
    print("正在进入.")
    print("登录成功")
    print("时间:3600年6月6日")
    print("地点:太平洋一个货轮上")
    print("事件:碰....糟糕触礁船翻了...救命..救...")
    print("...")
    print(".")
    time.sleep(1)
    print("斯...头好痛")
    xuan()
def print_d():
        print("1------开始探险")
        print("2------查看属性")
        print("3------查看物品")
        print("4------换购物品")
        print("5------补充能量")
        print("6------丢弃物品")
        print("0------退出系统")
def xuan():
    print("欢迎主人来到荒岛体验系统".center(50,"*"))
    tian()
    while True:
        print_d()
        a = input("请输入您的选择")
        if a.isdigit():
            a = int(a)
        else:
            print("登录失败")
        if a == 1:
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
            break
def tian():
    zi={}
    zi["jian"] = 100
    zi["shui"] = 100
    zi["ti"] = 100
    list3.append(zi)
def print_1():
    print("1---处级探险(可以获得水源,野果.木材)")
    print("2---高级探险(可以碰到猎物获得食物,草药,矿物)")
    print("0---取消探险")
    b = int(input("请输入选择"))
    zi={}
    yuan = 0
    rou = 0
    yao = 0
    kuang = 0
    shui = 0
    ye = 0
    cai = 0
    if b == 1:
        while True:
            a = random.randint(1,5)#1---水源 2----野果 3---木材 其他---什么也没有
            a = int(a)
            if a == 1:
                print_jian()
                yuan = random.randint(1,10)
                print("恭喜你获得了%d瓶水可补充水分"%yuan)
                yuan += yuan
                print("1------继续探险")
                print("2------退出探险")
                ji = int(input("请选择"))
                if ji == 2:
                    break
            elif a == 2:
                print_jian()
                ye = random.randint(1,10)
                print("恭喜你获得了%d个野果可补充少量体力"%ye)
                ye += ye
                print("1------继续探险")
                print("2------退出探险")
                ji = int(input("请选择"))
                if ji == 2:
                    break
            elif a == 3:
                print_jian()
                cai = random.randint(1,10)
                print("恭喜你获得了%d根木材可创造东西"%cai)
                cai+=cai
                print("1------继续探险")
                print("2------退出探险")
                ji = int(input("请选择"))
                if ji == 2:
                    break
            else:
                print("什么也没找到")
                print("1------继续探险")
                print("2------退出探险")
                ji = int(input("请选择"))
                if ji == 2:
                    break
    
    zi["yuan"] = yuan
    zi["ye"] = ye
    zi["cai"] = cai
                
    if b == 2:
        while True:
            a = random.randint(1,6)#1---碰到野兽2------找到草药3---找到矿物
            a = int(a)
            if a == 1:
                print_jian()
                print("碰到野兽")
                print("1---放弃战斗")
                print("2---继续战斗")
                xuan = int(input("请选择"))
                if xuan == 1:
                    break
                elif xuan == 2:
                    b = random.randint(1,2)#判断成功或失败
                    if b == 1:
                        rou = random.randint(1,5)
                        print("战斗成功获得%d块肉可以补充大量体力"%rou)
                        rou+=rou
                        print("1------继续探险")
                        print("2------退出探险")
                        ji = int(input("请选择"))
                        if ji == 2:
                            print("猎物逃跑了")
                            break 
            elif a == 2:
                print_jian()
                yao = random.randint(1,10)
                print("恭喜获得%d棵草药可以治疗"%yao)
                yao+=yao
                print("1------继续探险")
                print("2------退出探险")
                ji = int(input("请选择"))
                if ji == 2:
                    break
            elif a == 3:
                print_jian()
                kuang = random.randint(1,10)
                print("恭喜获得%d块矿物可创造东西"%kuang)
                kuang+=kuang
                print("1------继续探险")
                print("2------退出探险")
                ji = int(input("请选择"))
                if ji == 2:
                    break
            else:
                print("什么也没找到")
                print("1------继续探险")
                print("2------退出探险")
                ji = int(input("请选择"))
                if ji == 2:
                    break
    zi["rou"] = rou
    zi["yao"] = yao
    zi["kuang"] = kuang
    list2.append(zi)

def print_2():
    print("健康\t体力\t水分")
    for position,i in enumerate(list3):
        print(i["jian"],"\t",i["ti"],"\t",i["shui"])   
def print_jian():
    for position,i in enumerate(list3):
        i["jian"] = i["jian"]-3
        i["ti"] = i["ti"]-3
        i["shui"] = i["shui"]-3
        if i["jian"] < 20:
            print("j健康快到极限了")
            print("请尽快医治")
        elif i["ti"] < 10:
            print("体力快到极限了")
            print("请尽快补充体力")
        elif i["shui"] < 15:
            print("水分快到极限了")
            print("请尽快补充水分")
def print_3():
    print("水\t野果\t木材\t肉\t草药\t矿物")
    for position,i in enumerate(list2):
        print(i["yuan"],"\t",i["ye"],"\t",i["cai"],"\t",i["rou"],"\t",i["yao"],"\t",i["kuang"])

def print_4():
    while True:
        print("欢迎来到换购商店".center(50,"*"))
        print("本商店任何东西都需等价交换")
        print("换购的东西为木材或矿物")
        print("材料不同换购的数量也不同")
        print("1------水")
        print("2------肉")
        print("3------药")
        print("0------退出")
        a = int(input("请输入序号"))
        if a == 1:
           print_xuan()
        elif a == 2:
            xuan_1()
        elif a == 3:
            xuan_2()
        elif a == 0:
            break
        
def print_xuan():
    print("1------木材")
    print("1------矿物")
    b = int(input("请选择序号"))
    if b == 1:
        for position,i in enumerate(list2):
            if i["cai"] > 1:
                i["cai"] = i["cai"]-1
                i["yuan"] = i["yuan"]+10
                print("恭喜获得10瓶水")
            else:
                print("材料不够")
    elif b == 2:
        for position,i in enumerate(list2):
            if i["kuang"] >= 1:
                i["kuang"] = i["kuang"]-1
                i["yuan"] = i["yuan"]+20
                print("恭喜获得20瓶水")
            else:
                print("材料不够")
def xuan_1():
    print("1------木材")
    print("1------矿物")
    b = int(input("请选择序号"))
    if b == 1:
        for position,i in enumerate(list2):
            if i["cai"] >= 1:
                i["cai"] = i["cai"]-1
                i["rou"] = i["rou"]+10
                print("恭喜获得10块肉")
            else:
                print("材料不够")
    elif b == 2:
        for position,i in enumerate(list2):
            if i["kuang"] >= 1:
                i["kuang"] = i["kuang"]-1
                i["rou"] = i["rou"]+20
                print("恭喜获得20块肉")
            else:
                print("材料不够")
def xuan_2():
    while True:
        print("1------木材")
        print("1------矿物")
        b = int(input("请选择序号"))
        if b == 1:
            for position,i in enumerate(list2):
                if i["cai"] >= 1:
                    i["cai"] = i["cai"]-1
                    i["yao"] = i["yao"]+10
                    print("恭喜获得10棵药")
                else:
                    print("材料不够")
                    break
        elif b == 2:
            for position,i in enumerate(list2):
                if i["kuang"] >= 1:
                    i["kuang"] = i["kuang"]-1
                    i["rou"] = i["rou"]+20
                    print("恭喜获得20棵药")
                else:
                    print("材料不够")
                    break
def print_5():
    while True:
        print("1---使用水(可增加自身水份)")
        print("2---使用肉(可以增加体力)")
        print("3---使用药(可以增加健康值)")
        print("0----退出")
        a = int(input("请选择序号"))
        if a == 0:
            break
        elif a == 1:
            for position,i in enumerate(list2):
                if i["yuan"] >= 1:
                    i["yuan"] = i["yuan"]-1
                    for postion,j in enumerate(list3):
                        j["shui"] = j["shui"]+10
                        print("使用成功")
                        print("增加10点水份值")
                else:
                    print("材料不足")
            
        elif a == 2:
            for position,i in enumerate(list2):
                if i["rou"] >= 1:
                    i["rou"] = i["rou"]-1
                    for postion,j in enumerate(list3):
                        j["ti"] = j["ti"]+10
                        print("使用成功")
                        print("增加10点体力值")
                else:
                    print("材料不足")
        elif a == 3:
            for position,i in enumerate(list2):
                if i["yao"] >= 1:
                    i["yao"] = i["yao"]-1
                    for postion,j in enumerate(list3):
                        j["jian"] = j["jian"]+10
                        print("使用成功")
                        print("增加10点健康值")
                else:
                    print("材料不足")
                
cuang()

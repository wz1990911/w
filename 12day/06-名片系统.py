print("欢迎来到名片系统".center(50,"*"))
list1 = []
while True:
    zi = {}
    print("1:添加名片")
    print("2:查找名片")
    print("3:修改名片")
    print("4:删除名片")
    print("5:打印名片")
    print("0:退出")
    a  = input("请输入您的选择")
    if a.isdigit():
        a = int(a)
    else:
        print("输入错误")
    if a == 1:
        while True:
            name = input("请输入您要添加的名字")
            if len(name) > 4:
                print("太长请重新输入")
                continue
            else:
                break
        while True:
            zhi = input("请输入职位")
            if len(zhi) > 4:
                print("太长请重新输入")
                continue
            else:
                break
        while True:
            hao = input("请输入手机号")
            if len(hao) != 11 or hao.startswith("1") == False:
                print("手机号输入有误请重新输入")
                continue
            else:
                break
        zi["name"] = name
        zi["zhi"] = zhi
        zi["hao"] = hao
        list1.append(zi)
        print(list1)
        print("添加成功")
    elif a == 2:
        cha = input("请输入您要查找的名片")
        flag = 0
        for i in list1:
            if cha == i["name"]:
                print("姓名:%s\n职位:%s\n号码:%s\n"%(i["name"],i["zhi"],i["hao"]))
                flag = 1
                break
        if flag == 0:
            print("查无此人")
    elif a == 3:
        xiu = input("请输入您要修改的名片")
        flag = 0
        for j in list1:
            if xiu == j["name"]:
                print("1------修改名字")
                print("2------修改职位")
                print("3------修改号码")
                xiu = int(input("请选择:"))
                if xiu == 1:
                    l = input("请输入新的名字")
                    j["name"] = l
                    print(j["name"],j["zhi"],j["hao"])
                elif xiu == 2:
                    k = input("请输入新的职位")
                    j["zhi"] = k
                    print(j["name"],j["zhi"],j["hao"])
                elif xiu == 3:
                    p = input("请输入新号码")
                    j["hao"] = p
                    print(j["name"],j["zhi"],j["hao"])
                    flag = 1
        if flag == 0:
            print("查无此人")
    elif a == 4:
        shan = input("请输入要删除的人")
        flag = 0
        for position,l in enumerate(list1):
            if shan == l["name"]:
                flag = 1
                print("1:确定删除")
                print("2:取消删除")
                num_2 = int(input("请选择序号"))
                if num_2 == 1:
                    list1.pop(position)
                    print("删除成功")
                    print(list1)
                break
        if flag == 0:
            print("查无此人")
    elif a == 5:
        print("名字\t职位\t电话")
        for w in list1:
            print(" "+w["name"]+"\t "+w["zhi"]+"\t "+w["hao"])
    elif a == 0:
        break
    else:
        print("输入有误")

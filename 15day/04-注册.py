list1 = []
def print_zhuce(acc,pwd):
    user = {}
    if len(acc) == 11 and acc.startswith("1") and len(pwd) > 6:
        print("注册成功")
        user["acc"] = acc
        user["pwd"] = user
        list1.append(user)
        login1(acc,pwd)
def login1(acc,pwd)
if list1:
    for i in list1:
        if acc == i["acc"] and pwd == i["pwd"]:
            print("登陆成功")
        else:
            print("登录失败")

        
acc = input("请注册账号")
pwd = input("请输入密码")
print_zhuce(acc,pwd)
if list1:
    acc = input("请输入账号")
    paw = input("请输入密码")

def print_suan(x,y,z):
    if z == "+":
        print("和是%d"%(x+y))
    if z == "-":
        print("差是%d"%(x-y))
    if z == "*":
        print("积是%d"%(x*y))
    if z == "/":
        if x != 0:
            print("余数是%d"%(x/y))
print_suan(1,2,"+")

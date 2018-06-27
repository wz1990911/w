import time
def yiuxi():
    i = 0
    while True:
        i+=1
        if i%2 == 0:
            time.sleep(1) 
            print("像风走了十万里不忘归期")
        else:
            daima()
def daima():
    print("我喜欢你")
yiuxi()

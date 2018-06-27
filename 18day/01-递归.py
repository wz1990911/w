def di(num):
    if num == 1:
        return 1
    else:
        return num*di(num-1)
        
res=di(5)   
print(res) 

def a(a,b,c):
    res = c(1,2)
    return res    
c= lambda a,b:a+b
res = a(1,2,c)
print(res)

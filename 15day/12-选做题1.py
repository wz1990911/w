def suannian(yer,month,day):
    count = 0
    dayue = [1,3,5,7,8,10,12]
    xiaoyue = [4,6,9,11]
    for j in range(1,month):
        if j in dayue:
            count+=31
        if j in xiaoyue:
            count+=30
        if j ==2:
            if year%400 == 0 or (yer%4 ==0 and yer%100 !=0):
                count+=29
            else:
                count+=28
    count+=day
    print(count)
dates = "20180622"
year = int(dates[0:4])
month = int(dates[4:6])
day = int(dates[6:])
suannian(year,month,day)

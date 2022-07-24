x=int(input())                          #輸入值
y=x/12                                  #打
z=x%12                                  #剩餘個數
if  z!=0:                               #以餘數判斷是否整除
    print(int(y),"dozen and",int(z))
else:                                   #整除之情況
    print(int(y),"dozen")
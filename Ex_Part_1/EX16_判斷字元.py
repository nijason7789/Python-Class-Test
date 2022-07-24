n = input()
x= int(n)
y= list(n)
z= 0
if x<0 or x>1000000:    #判斷是是否為範圍內
    print('NO')

else:
    for i in range(len(y)): #逐字判斷是否為7
        if int(y[i])==7:
            print('YES')
            break
        else:   #若字元非7則判斷數字是否為7之倍數
            z=z+1
            if x%7==0:
                print('YES')
                break
            else:                
                if z==len(y):
                    print('NO')



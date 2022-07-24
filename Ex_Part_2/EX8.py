x = eval(input())
y = x//4            #正規可獲贈瓶數
s = 0               #舒跑數量
#四瓶蓋送一舒跑
#餘數為三可進位一次

if (x+y)%4 == 3:
    s = x+y+1
    print(s)
else:
    if y+x%4 > 4:
        s = x+y+1
        print(s)
    else:
        if (x+y)%4 ==0:
            s = x+y+1
            print(s)
        else:
            s = x+y
            print(s)
print(x,y) 

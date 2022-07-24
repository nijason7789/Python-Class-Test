P = [eval(i) for i in input().split()]
n = P[0]    #頭的總數
m = P[1]    #腳的總數
x = 0       #雞的初始值
y = 0       #兔的初始值

#x+y=n
#2x+4y=m
#2y=m-2n => y=(m-2n)/2
#2x=4n-m => x=(4n-m)/2

if (m-2*n)%2 != 0 or n==m: 
    print('NO')
else:
    x = (4*n-m)/2
    y = (m-2*n)/2
    print('YES')
    print(int(x),int(y))



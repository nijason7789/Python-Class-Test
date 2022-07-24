n = [eval(i) for i in input().split()]
L = n[0] #重點秒數
S = n[1] #現在秒數
#快轉一次5秒
#倒轉一次兩秒
#S+(5x-2y)=L,求x+y
x = 0
y = 0

while (L-S)!=(5*x-2*y):
    if (5*x-2*y)>(L-S):
        y=y+1
    else:
        x=x+1

print(x+y)

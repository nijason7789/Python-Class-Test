import math
#輸入三組座標
P1 = [eval(i) for i in input().split()]
P2 = [eval(i) for i in input().split()]
P3 = [eval(i) for i in input().split()]
#建立三角形之座標系統
ax = P1[0]
ay = P1[1]
bx = P2[0]
by = P2[1]
cx = P3[0]
cy = P3[1]
#由座標計算三邊長
A = math.sqrt((bx-ax)**2+(by-ay)**2)
B = math.sqrt((bx-cx)**2+(by-cy)**2)
C = math.sqrt((cx-ax)**2+(cy-ay)**2)
#計算半周長
S = (A+B+C)/2
#套入海龍公式
P = math.sqrt(S*(S-A)*(S-B)*(S-C))

print('%.2f'%P)
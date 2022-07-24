P = [eval(i) for i in input().split()]
N = P[0]       #比賽時間
X = P[1]        #加熱溫度
Y = P[2]        #減少溫度
T = 20          #室溫20度
Dish = 0        #最終溫度

if N%2 !=0:
    Dish = T+((N//2)+1)*X - (N//2)*Y    #加熱次數較多，故先加熱
    print(Dish)

else:
    Dish = T+((N//2))*X - ((N//2)-1)*Y  #第一分鐘不加熱，讓室溫掉零度
    print(Dish)

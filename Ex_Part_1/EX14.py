import math
x = eval(input())
print('Original: %.2f'%x)
print('Adjusted: %.2f(%+.0f)'%(math.sqrt(x)*10,10*math.sqrt(x)-x))
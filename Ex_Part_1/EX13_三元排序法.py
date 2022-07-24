x = eval(input())
y = eval(input())
z = eval(input())
avg = (x+y+z)/3
print('sum is',x+y+z)
print('average is %.2f'%avg)
print('product is', x*y*z)

if x>y:
    if y>z:
        print('smallest is',z)
        print('largest is',x)
    else:
        if x>z:
            print('smallest is',y)
            print('largest is',x)
        else:
            print('smallest is',y)
            print('largest is',z)
else:   #y>z
    if x>z:
        print('smallest is',z)
        print('largest is',y)
    else:
        if y>z:
            print('smallest is',x)
            print('largest is',y)
        else:
            print('smallest is',x)
            print('largest is',z)
            

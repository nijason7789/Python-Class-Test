##終極密碼
ans = int(input())  #First input is the answer
m = 100
n = 1
print(n,'< ? <',m)
x = int(input())

if x == ans:
    print('bingo answer is',x)
else:
    while x != ans:
        if x>=m or x<=n:
            print('out of range')
            print(n,'< ? <',m)
            x = int(input())
        if x < ans:
            n = x
            print('wrong answer, guess larger')
            print(n,'< ? <',m)
            x = int(input())
        if x > ans:
            m = x
            print('wrong answer, guess smaller')
            print(n,'< ? <',m)
            x= int(input())
        if x == ans:
            print('bingo answer is',x)
            quit()




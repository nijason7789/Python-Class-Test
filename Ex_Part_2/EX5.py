Score = eval(input())

if Score >= 95:
    print('獎金 2000 元')
else:
    if Score < 95 and Score >= 90:
         print('獎金 1000 元')
    else:
        if Score < 90 and Score >= 80:
            print('獎金 500 元')
        else:
            print('獎金 0 元')
School = eval(input())
Score = eval(input())

if Score >= 60:
    if School ==2 and Score < 70:
        print('fail')
    else:
        print('pass')
else:
    print('fail')
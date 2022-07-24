#先淘汰錯誤數據
School = eval(input())
if School < 1 or School >2:
    print('role error')   
    quit()

Score = eval(input())
if Score < 0 or Score > 100:
    print('score error')
    quit()


#開始判斷分數是否及格
if Score >= 60:
    if School == 2 and Score < 70:
        print('fail')
    else:
        print('pass')
else:
    print('fail')
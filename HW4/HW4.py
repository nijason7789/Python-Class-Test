Prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,1000] #建立質數表
x = eval(input()) #查詢之質數
i = 0
while Prime[i]<=x:
    print('%d is prime'%Prime[i])
    i=i+1
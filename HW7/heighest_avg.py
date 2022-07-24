'''
二維陣列
{76,73,85
 88,84,76
 92,82,92
 82,91,85
 72,74,73}

'''

A = [[76,73,85],[88,84,76],[92,82,92],[82,91,85],[72,74,73]]

i = 0
j = 0
k = 0
avg = 0.0
sumi = []
sumt = 0

for i in range(len(A)):
    print('student',i+1)
    print(' 1:',A[i][0])
    print(' 2:',A[i][1])
    print(' 3:',A[i][2])
    sum1 = A[i][0]+A[i][1]+A[i][2]
    print(' sum: %d'%sum1)
    sumi.append(sum1)
    avg = float(A[i][0]+A[i][1]+A[i][2])/3
    print(' avg: %.2f'%avg)
    i=i+1

for j in range(len(sumi)):
    sumt = sumt+sumi[j]


while sumi[k] < max(sumi):
    k = k+1
avgk = (A[k][0]+A[k][1]+A[k][2])/3
print('total: %d,'%sumt,'avg: %.2f'%(sumt/15))
print('highest avg: student %d:'%(k+1),'%.2f'%avgk)


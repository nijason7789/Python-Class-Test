'''
Math = [柯南,灰原,步美,美環,光彦]
English = [柯南,灰原,步美,丸尾,野口]
Student = [柯南,灰原,步美,丸尾,美環,野口,光彦]

柯南 = [1,1]
灰原 = [1,1]
步美 = [1,0]
丸尾 = [0,1]
美環 = [1,0]
野口 = [0,1]
光彥 = [1,0]
'''

MathPass = set(['柯南','灰原','步美','美環','光彦'])
EnglishPass = set(['柯南','灰原','步美','丸尾','野口'])

BothPass = []
OnlyMath = []
OnlyEnghlish = []

a = MathPass.intersection(EnglishPass)
b = MathPass.difference(EnglishPass)
c = EnglishPass.difference(MathPass)

BothPass = list(a)
OnlyMath = list(b)
OnlyEnghlish = list(c)

BothPass.sort()
OnlyMath.sort()
OnlyEnghlish.sort()



print(OnlyMath)
print(OnlyEnghlish)
print(BothPass)
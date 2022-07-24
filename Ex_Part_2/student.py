class student:
    
    def __init__(self,name,gender):
       self.name = name
       self.gender = gender
       self.grades = []
    
    def avg(self):
        return sum(self.grades)/len(self.grades)

    def add(self,score):
        self.grades.append(score)

    def fcount(self):
        k = 0
        fct = 0
        for k in range(len(self.grades)):
            if self.grades[k] < 60:
                fct = fct+1
            k=k+1
        return fct

    def show(self):
        print('Name:',self.name)
        print('Gender:',self.gender)
        print('Grades:',self.grades)
        print('Avg: %.1f'%self.avg())
        print('Fail Number: %d\n'%self.fcount())

def top(*student):
    MaxAvg = 0
    Maxi = 0
    for i in s1,s2,s3,s4,s5:
        if i.avg() > MaxAvg:
            MaxAvg=i.avg()
            Maxi = i
    print("Top Student:")
    Maxi.show()






s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)
 
s1.show()
s2.show()
s3.show()
s4.show()
s5.show()

top_student = top(s1,s2,s3,s4,s5)




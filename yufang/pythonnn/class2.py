class student:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
        self.grades=[]
    def add(self,score):
        self.grades.append(score)
    def avg(self):
        return sum(self.grades)/len(self.grades)
    def fcount(self):
        fct=0
        for i in self.grades:
            if i<60:
                fct+=1
        return fct
    def show(self):
        print('Name:',self.name)
        print('Gender:',self.gender)
        print('Grades:',self.grades)
        print('Avg:',self.avg())
        print('Fail Number:',self.fcount())
        print()
        



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

def top(*avgs):
    S=[]
    for i in avgs:
        S.append(i)
    n=S.index(max(S))+1
    print('Top Student:')    
    if n==1:
        s1.show()
    if n==2:
        s2.show()
    if n==3:
        s3.show()
    if n==4:
        s4.show()
    if n==5:
        s5.show()
    

top(s1.avg(),s2.avg(),s3.avg(),s4.avg(),s5.avg())

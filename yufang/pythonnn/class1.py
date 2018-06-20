class student:
    def __init__(self,na,gend):
        self.name=na
        self.gender=gend
        self.grades=[]
    def avg(self):
        return sum(self.grades)/len(self.grades)
    def add(self,score):
        self.grades.append(score)
    def fcount(self,score):
        fct=0
        if score<60:
            fct+=1
        return fct
    def show(self):
        print(self.name)
        print(self.avg())
        print(fct())

a=input()
b=input()
s1=student(a,b)
s1.add(eval(input())
s1.add(eval(input())
s1.add(eval(input())
        

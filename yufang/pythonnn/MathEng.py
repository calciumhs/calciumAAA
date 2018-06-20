m=open('../app/math_list.csv','r',encoding='Big5')
math=m.readlines()
m.close()

e=open('../app/english_list.csv','r',encoding='Big5')
eng=e.readlines()
e.close()

M=[]
E=[]

for i in range(len(math)):
    M.append(math[i][0:9])
    E.append(eng[i][0:9])

M=set(M[1:])
E=set(E[1:])
u=M.union(E)
i=M.intersection(E)
    

a=list(i)
a.sort()
b=list(u-i)
b.sort()
c=list(M-i)
c.sort()
d=list(E-i)
d.sort()
e=list(u)
e.sort()

 
print(a)
print(b)
print(c)        
print(d)
print(e) 
        
        
        


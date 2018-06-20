f1=open('score.txt','r')
t1=f1.readlines()
f1.close()
P=[]
F=[]
for i in range(1,len(t1)):
    t1[i]=t1[i].strip().split(',')
    t1[i][1]=eval(t1[i][1])
    t1[i][2]=eval(t1[i][2])
    if t1[i][1]>=60 and t1[i][2]>=60:
        P.append(t1[i][0])
    elif (t1[i][1]+t1[i][2])<120:
        F.append(t1[i][0])
        
P.sort()
F.sort()

print(P)
print(F)
print(len(t1)-1)
      

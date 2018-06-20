one=input()
two=input()
one='../app/'+one
two='../app/'+two

f1=open(one,'r')
t1=f1.readlines()
f1.close()

f2=open(two,'r')
t2=f2.readlines()
f2.close()

A=[]
N=[]
for i in range(1,len(t1)):
    t1[i]=t1[i].strip().split(',')
    t2[i]=t2[i].strip().split(',')
    a=eval(t2[i][1])-eval(t1[i][1])
    A.append(a)

m=max(A)

while True:
    if m in A:
        n=A.index(m)
        A[n]=0
        N.append(t1[n+1][0])
    else:
        break

print('Dark Horse: ',end='')
for i in N[0:len(N)-1]:
    print(i,end=' & ')
print(N[-1])
print('%.1f'%m,'Points Progress')
    

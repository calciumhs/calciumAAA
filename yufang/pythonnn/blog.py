a=input()
b=input()
a='../app/'+a
b='../app/'+b
f1=open(a,'r')
t1=f1.readlines()
f1.close()

f2=open(b,'r')
t2=f2.readlines()
f2.close()

T1=t1[0].strip().split()
T2=t2[0].strip().split()

T=[]
for i in range(len(T1)):
    T.append(eval(T1[i]))
for i in range(len(T2)):
    T.append(eval(T2[i]))

T.sort()

for i in range(len(T)):
    print(T[i],end=' ')
print()

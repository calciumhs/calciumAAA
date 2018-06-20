mid=input()
fin=input()


f1=open(mid,'r')
M=f1.readlines()
f1.close()

f2=open(fin,'r')
F=f2.readlines()
f2.close()

for i in range(len(M)):
    M[i]=M[i].split()
    F[i]=F[i].split()
    


print(M)
print(F)

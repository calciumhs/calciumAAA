b=[]
c=[]
u=0
for j in range(1,6):
    a=[eval(i) for i in input().split()]
    b.append(a)

for i in range(1,6):
    x=sum(b[i-1])
    y=sum(b[i-1])/3
    print('student %d'%i)
    print(' 1: %d'%(b[i-1][0]))
    print(' 2: %d'%(b[i-1][1]))
    print(' 3: %d'%(b[i-1][2]))
    print(' sum: %d'%x)
    print(' avg: %.2f'%y)
    u+=x
    c.append(y)
    
v=u/15
m=max(c)
n=c.index(m)+1

print('total: %d, avg: %.2f'%(u,v))
print('highest avg: student %d: %.2f'%(n,m))

    
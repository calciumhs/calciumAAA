a=[]
b=[]
c=[[0,0,0],[0,0,0],[0,0,0]]

for j in range(3):
    a1=[eval(i) for i in input().split()]
    a.append(a1)

for j in range(3):
    b1=[eval(i) for i in input().split()]
    b.append(b1)
    
def matrixMultiPly(a, b):
    for i in range(3):
        c[i][0]=a[i][0]*b[0][0]+a[i][1]*b[1][0]+a[i][2]*b[2][0]
        c[i][1]=a[i][0]*b[0][1]+a[i][1]*b[1][1]+a[i][2]*b[2][1]
        c[i][2]=a[i][0]*b[0][2]+a[i][1]*b[1][2]+a[i][2]*b[2][2]
    return c

c=matrixMultiPly(a, b)

print(c[0])
print(c[1])
print(c[2])    

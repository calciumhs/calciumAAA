a=eval(input())
n=[eval(i) for i in input().split()]
b=eval(input())
m=[eval(j) for j in input().split()]
m.sort()

nn=n.copy()

if 0 in m:
    m.remove(0)
    '''
    for x in range(b-2,-1,-1):
        y=m[x]-1
        n.pop(y)
    '''

'''
else:

    for x in range(b-1,-1,-1):
        y=m[x]-1
        n.pop(y)
'''

for i in m:
    n[i-1]=0
    '''
c=max(n)
d=nn.index(c)+1

print(sum(n))
print(d,c)
'''

print(sum(n))
Max = max(n)
Index = n.index(Max) +1
print(Index,Max)

    

def sum1(n):
    tf=1
    for i in range(1,n+1):
        tf *= i
    return tf

def P(n,m):
    return int(sum1(n)/sum1(n-m))

def C(n,m):
    return int(P(n.m)/sum1(m))



x=eval(input())
y=eval(input())
print(P(x,y))
print(C(x,y))




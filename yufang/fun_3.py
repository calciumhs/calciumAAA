def return2num(n=0):
    ts=0
    tf=1
    for i in range(1,n+1):
        ts += i
        tf *= i
    return ts,tf


x=eval(input())
ans=return2num(x)

print(ans[1])
print(ans[0])



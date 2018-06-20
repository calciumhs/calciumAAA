a=eval(input())
n=[eval(i) for i in input().split()]

big=max(n)
sma=min(n)

bb=n.index(big)+1
ss=n.index(sma)+1
print('%d %d'%(bb,big))
print('%d %d'%(ss,sma))

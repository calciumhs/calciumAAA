import time

t=eval(input())

x=time.gmtime(t)
y=time.localtime(t)
print(time.strftime('%Y-%m-%d %H:%M:%S',x))
print(time.strftime('%Y-%m-%d %H:%M:%S',y))

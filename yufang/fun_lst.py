lst=[]

while True:
    n=eval(input())
    if n==-1:
        break
    else:
        lst.append(n)

lst.sort()
print(lst[-3])

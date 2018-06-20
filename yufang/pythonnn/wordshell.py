
lst=[]
length=[]

while True:
    a=input()
    if a=='-1':
        break
    else:
        lst.append(a)
        b=len(a)
        length.append(b)
        continue

c=input()

n=max(length)+2

for i in range(n):
    print(c,end='')
print()

for j in range(len(lst)):
    print(c,end='')
    print(lst[j],end='')
    m=max(length)-len(lst[j])
    for k in range(m):
        print(' ',end='')
    print(c)
    
for i in range(n):
    print(c,end='')
print()


        

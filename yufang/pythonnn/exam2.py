A=[]
while True:
    a=input()
    if a=='-1':
        break
    else:
        try:
            a=eval(a)
            A.append(a)
        except:
            continue
x=sum(A)
z=len(A)
y=x/z

print('%.2f'%x)
print('%.2f'%y)
print(z)

lst=[]
while True:
    try:
        n=eval(input())
        if n==-1:
            break
        lst.append(n)
        del n
    except:#有錯誤就跳過(跳過非數字的NA)
        continue

     
a=sum(lst)
b=len(lst)
c=a/b

print('%.2f'%a)
print('%.2f'%c)
print('%d'%b)
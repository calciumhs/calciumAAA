def swap(lst):
    lst.reverse()
    return lst

a=input()
b=input()
LL=[]
LL.append(a)
LL.append(b)
swap(LL)
print(LL[0])
print(LL[1])

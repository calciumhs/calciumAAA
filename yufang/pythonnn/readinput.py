a=input()

f=open(a,'r',encoding='big5')
txt=f.readlines()
f.close()

for i in range(len(txt)):
    txt[i]=txt[i].split()
    print(txt[i])

f=open('stores_old.csv','r',encoding='Big5')
txt=f.readlines()
f.close()

for i in range(len(txt)):
    txt[i]=txt[i].split()
    print(txt[i])

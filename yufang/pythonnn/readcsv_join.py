f=open('store_old.csv','r',encoding='big5')
txt=f.readlines()
f.close()

for i in range(len(txt)):
    txt[i]=txt[i].split(',')


f2=open('store_new.csv','w')
for i in range(len(txt)):
    f2.write(','.join(txt[i])
f2.close()

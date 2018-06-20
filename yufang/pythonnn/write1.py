f1=open('./stores_old.csv','r',encoding='big5')
txtLst=f1.readlines()
f1.close()

for i in range(len(txtLst)):
    txtLst[i]=txtLst[i].strip().split(',')

f2=open('./stores_new.csv','w',encoding='utf-8')
for i in range(len(txtLst)):
    for j in range(len(txtLst)):
        if j==0 or j==3 or j==5 or j==6:
            f2.write(txtLst[i][j])
            f2.write(',')
    f2.write('\n')
f2.close()


f3=open('./stores_new.csv','r',encoding='utf-8')
txtLst2=f3.readlines()
f3.close()

for i in range(len(txtLst2)):
    txtLst2[i]=txtLst2[i].strip()
    print(txtLst2[i])

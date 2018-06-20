f=open('../app/sim.txt','r',encoding='gb2312')
txt=f.readlines()
f.close()

print(txt[0][0:8])
for i in range(1,len(txt)):
    print(txt[i][0:12])

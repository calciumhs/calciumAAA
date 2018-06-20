f1=open('score.txt')
SS=f1.readlines()
f1.close()


for i in range(len(SS)):
    SS[i]=SS[i].strip()
    print(SS[i])

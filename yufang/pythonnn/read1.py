a=open('longhate.txt',encoding='big5')
t=a.readlines()
a.close()
 
for i in range(len(t)):
    t[i]=t[i].strip()
    print(t[i])

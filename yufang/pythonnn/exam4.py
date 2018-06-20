import math
import string
ABC=string.ascii_lowercase

f1=open('postit.txt','r',encoding='Big5')
t1=f1.readlines()
f1.close()

for i in range(len(t1)):
    t1[i]=t1[i].strip().split('-')
    for j in range(len(t1[i])):
        t1[i][j]=eval(t1[i][j])
        t1[i][j]=int(math.sqrt(t1[i][j]))
        a=t1[i][j]-1
        t1[i][j]=ABC[a]

for i in range(len(t1)):
    for j in range(len(t1[i])):
        print(t1[i][j],end='')
    print(' ',end='')

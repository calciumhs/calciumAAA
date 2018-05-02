DD={'A':10,'J':18,'S':26,
 'B':11,'K':19,'T':27,
 'C':12,'L':20,'U':28,
 'D':13,'M':21,'V':29,
 'E':14,'N':22,'W':32,
 'F':15,'O':35,'X':30,
 'G':16,'P':23,'Y':31,
 'H':17,'Q':24,'Z':33,
 'I':34,'R':25}

a=input()
aa=list(a)
b=DD[aa[0]]




b=eval(DD[aa[0]])
c=(b//10)*1+(b%10)*9
z=0
for i in range(1,10):
    x=eval(aa[i])
    y=x*(9-i)
    z+=y

if (c+z)%10==0:
    print('real')
else:
    print('fake')





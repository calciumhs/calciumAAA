Dic={'A':10,'J':18,'S':26,
 'B':11,'K':19,'T':27,
 'C':12,'L':20,'U':28,
 'D':13,'M':21,'V':29,
 'E':14,'N':22,'W':32,
 'F':15,'O':35,'X':30,
 'G':16,'P':23,'Y':31,
 'H':17,'Q':24,'Z':33,
 'I':34,'R':25}

a=input()
y=0
if len(a)!=10:
    print('fake')
else:
    a=a.upper()
    b=Dic[a[0]]
    x=b//10+b%10*9
    
    for n in range(1,9):
        c=eval(a[n])
        d=c*(9-n)
        y+=d
        
    z=eval(a[9])+y+x
    
    if z%10==0:
        print('real')
    else:
        print('fake')
        


booklist=[]
b=input()
b=b.upper()

while True:
    a=input()
    if a=='q':
        break
    else:
        a=a.upper()
        booklist.append(a)


if b in booklist:
    numY=booklist.index(b)+1
    print('Yes %d'%numY)
else:
    numN=len(booklist)
    print('No %d'%numN)
        

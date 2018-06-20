D={'P':'Pikachu','M':'Mickey Mouse','H':'Hello kitty'}

while True:
    a=input()
    if a=='-1':
        break
    else:
        if a in D:
            print(D[a])
            
        else:
            print(a,'does not exist. Enter a new one:')
            D[a]=input()
            
            
    

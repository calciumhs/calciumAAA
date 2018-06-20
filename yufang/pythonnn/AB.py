ans=input()
a=0
b=0
while True:
    g=input()
    if g==ans:
        print('4A0B')
        print('You Win!')
        break
    else:
        for i in range(4):
            if g[i]==ans[i]:
                a+=1
            else:
                if g[i] in ans:
                    b+=1

        print('%dA%dB'%(a,b))
        a=0
        b=0
        

    
                    
                

LEFT = ['(','[','{','<']
RIGHT = [')',']','}','>']
RIGHT_dic = {')':'(',']':'[','}':'{','>':'<'}

n=eval(input())
X=[]
for w in range(n):
    x = input()    
    X.append(x)

for w in range(n):

    Y=X[w]
    TEST = []
    for i in Y:
        if i in LEFT:
            TEST.append(i)
        if i in RIGHT:
            if TEST==[]:
                TEST.append('n')
            elif TEST[-1] == RIGHT_dic[i]:
                TEST[-1] = ''
                TEST.remove('')
            elif TEST[-1] != RIGHT_dic[i]:
                TEST.append('n')
            
    if TEST==[]:
            print('Y')
    else:
            print('N')


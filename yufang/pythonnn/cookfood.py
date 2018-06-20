n = int(input())
Ind = []
for i in range(n):
    Ind.append(input().strip().split())
    
ind = []
for i in Ind:
    ind.append(i[0])
ind = list(set(ind))

Ind2 =[]
for i in ind:
    number = 0
    for j in Ind:
        if i == j[0]:
            number += int(j[1])
    Ind2.append([i,number])        

Ind3 = sorted(Ind2, key = lambda x : x[1],reverse=True)
    
print(Ind3[0][0],Ind3[0][1])

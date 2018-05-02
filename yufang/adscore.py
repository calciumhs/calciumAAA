import math

a=eval(input())
b=math.sqrt(a)*10
c=round(b-a)

print('Original: %.2f'%a)
print('Adjusted: %.2f(+%d)'%(b,c))



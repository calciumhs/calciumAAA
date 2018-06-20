import os

n=eval(input())

if os.path.exists('files'):
    os.chdir('files')
    for i in os.listdir():
        os.rmdir(i)
    os.chdir('../')
    os.rmdir('files')

os.mkdir('files')
os.chdir('files')

for i in range(1,n+1):
    os.mkdir('f'+str(i))

p1=os.listdir()
p1.sort()
print(p1)

os.rename('f1','folder1')
p1=os.listdir()
p1.sort()
print(p1)

os.rmdir('folder1')
p1=os.listdir()
p1.sort()
print(p1)

for i in os.listdir():
    os.rmdir(i)
    
os.chdir('../')
os.rmdir('files')

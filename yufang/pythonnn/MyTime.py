import time

def GetTime(fmt):
    return time.strftime(fmt)

st=GetTime('%Y-%m-%d %H:%M:%S') 
print(st)
ipt=time.time()

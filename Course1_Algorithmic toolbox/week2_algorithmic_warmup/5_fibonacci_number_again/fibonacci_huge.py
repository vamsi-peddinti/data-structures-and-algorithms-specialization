# Uses python3
import numpy as np
n=[]
length, mod=map(int,input().split())
if length==0:
    n.append(0)
    ans=0
else:
    n.append(0)    
    n.append(1)
    if length==1:
        ans=1
    for i in range(2,length+1):
        newelement=(n[i-1]+n[i-2])%mod
        n.append(newelement)
    ans=newelement
print(ans)


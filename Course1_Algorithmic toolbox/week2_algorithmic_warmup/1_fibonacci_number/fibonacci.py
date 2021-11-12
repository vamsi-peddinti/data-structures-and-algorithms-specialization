# Uses python3
import numpy as np
n=[]
length=int(input())
if length==0:
    n.append(0)
    ans=0
else:
    n.append(0)    
    n.append(1)
    if length==1:
        ans=1
    for i in range(2,length):
        newelement=n[i-1]+n[i-2]
        n.append(newelement)
    ans=(n[-1]+n[-2])
print(ans)
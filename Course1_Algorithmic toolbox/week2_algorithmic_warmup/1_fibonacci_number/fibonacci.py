# Uses python3
n=[]
length=int(input())
n.append(0)
n.append(1)
sum=0
for i in range(2,length):
    n[i]=n[i-1]+n[i-2]
    sum=n[i]
print(sum)
#O(n**2) solution
l=list(map(int,input().split()))
n=len(l)
dp=[1]*n
for i in range(1,n):
    for j in range(i):
        if l[i]>=l[j]:
            dp[i]=max(dp[i],dp[j]+1)
print(max(dp))

#O(n*log(n)) solution
def search(i):
    l=0
    r=len(active)-1
    while l<r-1:
        m=l+(r-l)//2
        if active[m]>=i:
            r=m
        else:
            l=m
    return r

active=[l[0]]
for i in l[1::]:
    if i<active[0]:
        active[0]=i
    elif i>active[-1]:
        active.append(i)
    else:
        active[search(i)]=i
print(len(active))
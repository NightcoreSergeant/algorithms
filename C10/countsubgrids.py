##O(n**3/N)
import time
def count(k): #in c++ use __builtin_popcount(k) runs in O(1)
    c=0
    for i in range(N):
        if k&1<<i:
            c+=1
    return c
start=time.time()
n=int(input())
g=[]
N=64
c=n//N+1
if n%N==0:
    c-=1
for i in range(n):
    s=input()
    g.append([])
    for j in range(c):
        k=0
        _from=j*N
        _to=min((j+1)*N,n)
        for i in range(_from,_to): 
            if s[i]=='1':
                k+=1<<i%N
        g[-1].append(k)

ans=0
for a in range(n-1):
    for b in range(a+1,n):
        cnt=0
        for i in range(c):
            cnt+=count(g[a][i]&g[b][i])
        ans+=(cnt-1)*cnt//2
end=time.time()
print(ans)
print(end-start)
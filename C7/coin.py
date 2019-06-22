#n=int(input())
#l=list(map(int,input().split()))
l=[1,3,5,10,13,7]
k=len(l)
n=561
inf=10**9
dp=[0 for i in range(n+1)]
history=[0 for i in range(n+1)]
for i in range(1,n+1):
    dp[i]=inf
    for j in l:
        if i-j>=0 and dp[i-j]+1<dp[i]:
            dp[i]=dp[i-j]+1
            history[i]=j
#print(dp)
#history
while i>0:
    print(history[i],end=' ')
    i-=history[i]

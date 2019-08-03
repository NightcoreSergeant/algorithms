k=int(input())
w=list(map(int,input().split()))
dp=[0 for i in range(sum(w)+1)]
dp[0]=1
for i in range(k):
    for j in range(len(dp)-1-w[i],-1,-1):
        if dp[j]:
            dp[w[i]+j]=1
print(dp)

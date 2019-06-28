c=list(map(int,input().split()))
n=int(input())
dp=[0]*(n+1)
dp[0]=1
for i in range(1,n+1):
    for j in c:
        if i>=j:
            dp[i]+=dp[i-j]
print(dp)

x=11 #target value
l=[1,2,3,4,5] #coins to use
n=len(l)
## memory O(N*X)
#dp=[[0 for j in range(x+1)] for i in range(n)]
#dp[0][0]=1
#for i in range(n):
#    for j in range(x+1):
#        if j>=l[i]:
#            dp[i][j]=dp[i][j-l[i]]+dp[i-1][j]
#        else:
#            dp[i][j]=max(dp[i-1][j],dp[i][j])
#print(dp[-1][-1])

## recursive
#def f(s,k):
#    if s==0:
#        return 1
#    elif s<0 or k==-1:
#        return 0
#    else:
#        return f(s-l[k],k)+f(s,k-1)
#
#print(f(x,n-1))

## memory O(X)
dp=[0 for i in range(x+1)]
dp[0]=1
for i in range(n):
    for j in range(1,x+1):
        if j-l[i]>=0:
            dp[j]+=dp[j-l[i]]
print(dp[-1])

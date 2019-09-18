def anccestor(x,k):
    for i in range(63,-1,-1):
        if k&1<<i:
            x=dp[i][x]
    return x

n,m=map(int,input().split())
n+=1
link=[0]*(n)
for i in range(m):
    a,b=map(int,input().split())
    link[b]=a
x=5
dp=[[0]*n for i in range(x)]

for i in range(n):
    dp[0][i]=link[i]

for i in range(1,x):
    for j in range(n):
        z=dp[i-1][j]
        dp[i][j]=dp[i-1][z]

for i in dp:
    print(*i)

while True:
    a,b=map(int,input().split())
    print(anccestor(a,b))
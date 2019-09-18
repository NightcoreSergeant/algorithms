#O(n**3)
n,m=map(int,input().split())
inf=float('inf')
g=[[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        g[i][j]=inf if i!=j else 0
for i in range(m):
    a,b,w=map(int,input().split())
    g[a][b]=w
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j]=min(g[i][j],g[i][k]+g[k][j])
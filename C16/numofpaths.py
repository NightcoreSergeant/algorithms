#O(!n)
def dfs(v):
    visited[v]=1
    for i in g[v]:
        ans[i]+=dfs(i)
    return 1
n,m=map(int,input().split())
x,y=map(int,input().split())
g=[[] for i in range(n)] #path from x -> y
ans=[0]*n
visited=[0]*n
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    #g[b+n].append(a)

dfs(x-1)
print(ans[y-1])
print(ans)

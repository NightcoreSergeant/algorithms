def dfs(a):
    visited[a]=True
    for b in g[a]:
        if visited[b]:
            continue
        dfs(b)
    return ans.append(a)

        
n,m=map(int,input().split())
g=[[] for i in range(n)]
r=[[] for i in range(n)]
visited=[False]*n
ans=[]

for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    g[a].append(b)
for i in range(n):
    if visited[i]:continue
    dfs(i)
ans=list(map(lambda x:x+1,ans))
print(*ans)
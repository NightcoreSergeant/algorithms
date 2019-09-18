#O(n+m)
#strong connected graph is a graph where you can from any node visit any other node
#strongly connected commponent is part of graph from within component you can visit any other node within

def dfs1(a):
    visited[a]=True
    for b in g[a]:
        if visited[b]:
            continue
        dfs1(b)
    order.append(a)

def dfs2(a,c):
    visited[a]=True
    for b in r[a]:
        if visited[b]:
            continue
        dfs2(b,c)
    components[c].append(a)
    
components={}
n,m=map(int,input().split())
g=[[] for i in range(n)]
r=[[] for i in range(n)]



for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    g[a].append(b)
    r[b].append(a)

visited=[False]*n
order=[]
for i in range(n):
    if visited[i]:
        continue
    dfs1(i)
    
visited=[False]*n
order.reverse()
print(order)
j=0
for i in range(n):
    if not visited[order[i]]:
        components[j]=[]
        dfs2(order[i],j)
        j+=1
for i in components:
    print(i,components[i])
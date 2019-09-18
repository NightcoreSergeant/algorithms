#lowest common ancestor
#method1 O(nlogn) preproces O(logn) querry
def dfs(v,u,l=l,time=time):
    tin[v]=time
    time+=1
    for i in range(1,l):
        up[i][v]=up[i-1][up[i-1][v]]

    for i in g[v]:
        if u!=i:
            dfs(u,i)
    tout[v]=time
    time+=1

def isa(a,b):
    return tin[a]<tin[b] and tout[a]>tout[b]

def lca(a,b):
    if isa(a,b):
        return a
    elif isa(b,a):
        return b
    for i in range(l-1,-1,-1):
        if isa(up[a][i],b):
            a=up[a][i]
    return up[a][0]
    
n,m=map(int,input().split())
link=[0]*n
g=[[] for i in range(n)]
log=[-1]
for i in range(n+1):
    log.append(log[i//2]+1)

for i in range(m):
    a,b=map(int,input())
    link[b]=a
    g[a].append(b)
    
time=0
tin=[0]*n
tout=[0]*n
l=log[n]+1 if log[n]!=log[n-1] else log[n]
up=[[0]*n for i in range(l)]
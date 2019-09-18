#O(nlog(m))
import heapq

n,m=map(int,input().split()) #number of nodes #number of edges
x,y=map(int,input().split()) #shortest path between x -> y
x,y=x-1,y-1
g=[[] for i in range(n)]
for i in range(m):
    a,b,w=map(int,input().split())
    a,b=a-1,b-1
    g[a].append((b,w))

inf=float('inf')
distance=[inf]*n
distance[x]=0

quee=[]
heapq.heappush(quee,(0,x))
visited=[False]*n
while quee:
    _,a=heapq.heappop(quee)
    if visited[a]:continue
    visited[a]=True
    for b,w in g[a]:
        if distance[b]>distance[a]+w:
            distance[b]=distance[a]+w
            heapq.heappush(quee,(distance[b],b))
print(distance)

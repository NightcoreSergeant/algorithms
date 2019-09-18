#O(!n)
n,m=map(int,input().split()) #number of nodes #number of edges
x,y=map(int,input().split()) #shortest path between x -> y
inf=float('inf')
edges=[]
for i in range(m):
    a,b,w=map(int,input().split()) # node a -> b with weight w
    edges.append((a,b,w))
distance=[inf]*n
distance[x]=0
for i in range(n):
    for a,b,w in edges:
        distance[b]=min(distance[b],distance[a]+w)

print(distance[y])
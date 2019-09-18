import heapq

def dfs(a,x):
	print('h')
	for b,w in g[a]:
		if x+w>mdist:continue
		#ans[b]+=1
		#dfs(b,x+w)
		ans[b]+=dfs(b,x+w)
	return 1


n,m=map(int,input().split()) 
x,y=map(int,input().split()) #path from x->y
x,y=x-1,y-1
inf=float('inf')

g=[[] for i in range(n)]
dist=[inf]*n
dist[x]=0
visited=[False]*n

quee=[]
for i in range(m):
	a,b,w=map(int,input().split())
	a,b=a-1,b-1
	g[a].append((b,w))

heapq.heappush(quee,(0,x))
while quee:
	_,a=heapq.heappop(quee)
	if visited[a]:
		continue
	visited[a]=True
	for b,w in g[a]:
		if dist[b]>dist[a]+w:
			dist[b]=dist[a]+w
			heapq.heappush(quee,(dist[b],b))

mdist=dist[y]
ans=[0]*n
#ans[x]=1
dfs(x,0)
print(ans)
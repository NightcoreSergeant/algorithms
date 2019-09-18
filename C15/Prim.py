#O(n+mlogm)
import heapq
inf=float('inf')
n,m=map(int,input().split())
g=[[] for i in range(n)]
link=[i for i in range(n)]
for i in range(m):
    a,b,w=map(int,input().split())
    g[a].append((w,b))
quee=[i for i in g[0]]
heapq.heapify(quee)
s=set()
s.add(0)
ans=0
while len(s)!=n:
    a,w1=heapq.heappop(quee)
    if a in s:
        continue
    s.add(a)
    ans+=w1
    for w2,b in g[a]:
        if b in s:
            continue
        heapq.heappush(quee,(w2,b))


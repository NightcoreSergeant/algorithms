##spaning trees
#O(mlogn)
from unionfind import *
import heapq
n,m=map(int,input().split())
edges=[]
link=[i for i in range(n)]
siz=[1]*n
for i in range(m):
    a,b,w=map(int,input().split())
    edges.append((a,b,w))
edges.sort(key=lambda x:x[2])
ans=0
for a,b,w in edges:
    if not same(a,b):
        unite(a,b)
        ans+=w
from collections import Counter
import heapq

def rec(level,p,s):
    w,l,r=tree[level][p]
    if l==r:
        print(key[l],s)
        d[key[l]]=s
        return 0
    rec(level-1,r,s+'1')
    rec(level-1,l,s+'0')

s=input()
d=Counter(s)
tree=[]
p=[]
key=[i for i in d]
for i,letter in enumerate(key):
    w=d[letter]
    heapq.heappush(p,(w,i,i,-1)) #weight, leftchild, rightchild, level of node..set to -1 because we don't know on which level node might be.

heapq.heapify(p)

while len(p)!=1: #all can be done without weight appending to a tree..it's more readable
    l,cl1,cl2,level1= heapq.heappop(p) #cl -> short for child left
    r,cr1,cr2,level2 = heapq.heappop(p)

    level=max(level1,level2)+1
    if len(tree)<=level:
        tree.append([])
    
    tree[level].append((l,cl1,cl2))
    tree[level].append((r,cr1,cr2))
    position=len(tree[level])

    heapq.heappush(p,(l+r,position-2,position-1,level))

tree.append([heapq.heappop(p)[:3]])
#for i in tree:
#   print(*i)

rec(len(tree)-1,0,'')
out=''
for i in s:
    out+=d[i]
print('compressed:',out)
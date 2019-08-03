#binary indexed tree - fenwick tree
#O(n) or O(nlog(n)) preproces
#O(log(n)) query
#O(log(n)) update
def p(k):
    return k&-k
def add(k,v):
    while k<=n:
        tree[k]+=v
        k+=p(k)

def sumq(k):
    s=0
    while k>=0:
       s+=tree[k]
       k-=p(k)
    return s
#def sumpref(a,b):
#    return pref[b]-pref[a]


a=[9,4,7,2,8,6,5,1];n=len(a)+1
tree=[0]*n

#!!BUILDING TREE!!#
#####
#for i in range(1,n): #O(nlog(n))
#    add(i,a[i-1])

#####
#pref=[0] 
#for i in a: #O(n) takes little more space
#    pref+=[pref[-1]+i]
#for k in range(1,n):
#    tree[k]=sumpref(k-p(k),k)

#####
tree=a.copy()
for i in range(1,n+1): #memory efficient
    k = i + (i & -i) # Finds next higher index that this value should contribute to
    if k <= n:
        tree[k] += tree[i]

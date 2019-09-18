def update(a,k):
    while a<=n:
        value[a]+=k
        a=a+p(a)

def path(a):
    s=0
    while a!=0:
        s+=value[a]
        a=p(a)
    return s

def sumq(a,b):
    return path(b)-path(a-1)

def p(k):
    return k&-k

def traverse(a):
    traversal.append(a)
    for b in g[a]:
        traverse(b)

def calcsiz(a):
    for b in g[a]:
        siz[a]+=calcsiz(b)
    return siz[a]

def sumqsubtree(a):
    x=siz[a]
    i=link[a]
    y=x+i
    return sumq(x,y)

n,m=map(int,input().split())
g=[[] for i in range(n)]
value=[0]*(n+1) #node values


for i in range(m):
    a,b,w=map(int,input().split())
    a,b=a-1,b-1
    g[a].append(b)

traversal=[]
siz=[1]*n #size of subtree

traverse(0)
calcsiz(0)

for i in range(n):
    a,w=map(int,input().split())
    value[a]=w

#change value to BIT
log=[-1]
for i in range(n+1):
    log.append(log[i//2]+1)
x=log[n]
for i in range(n-x):
    value.append(0)

for i in range(1,n+1):
    k=i+(-i&i)
    if k<=n:
        value[k]+=value[i]

#set links
link=[0]*n
for i in range(len(traversal)):
    link[traversal[i]]=i


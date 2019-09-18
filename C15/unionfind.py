#O(log(n))
def find(a): #find root
    while a!=link[a]:
        a=link[a]
    return a
    
def same(a,b):
    return find(a)==find(b)

def unite(a,b):
    a=find(a)
    b=find(b)
    if siz[a]<siz[b]:
        a,b=b,a
    link[b]=a
    siz[a]+=siz[b]
link=[]
siz=[]
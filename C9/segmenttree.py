#preproces O(n)
#queries O(log(n))
#update O(log(n))
def add(k,x):
    k+=n
    tree[k]+=x
    #k=k//2
    while k!=1:
        k//=2
        tree[k]=tree[2*k]+tree[2*k+1]
def sum(a,b):
    global n
    s=0
    a+=n;b+=n
    while a<=b:
        if a%2==1:
            s+=tree[a];a+=1
        if b%2==0:
            s+=tree[b];b-=1
        b//=2
        a//=2

a=[5,8,6,3,2,7,2,6];n=len(a)
tree=[0]*(2*n)

for i in range(n): #construction O(n)
    tree[i+n]=a[i]
for i in range(n-1,0,-1):
    tree[i]=tree[i*2]+tree[i*2+1]

print(tree)
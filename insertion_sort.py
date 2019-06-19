l=list(map(int,input().split()))
for j in range(1,len(l)):
    key=l[j]
    i=j-1
    while i>0 and l[i] > key:
        l[i+1] = l[i]
        i-=1
    l[i+1]=key
print(l)
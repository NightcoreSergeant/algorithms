#recursion O(2**n)
#def search(k,s):
#    if k==n:
#        print(*s)
#        return 0
#    search(k+1,s)
#    s.append(k)
#    search(k+1,s)
#    s.pop()
n=3
#search(0,[])
for i in range(2**n):
    s=[]
    for j in range(n):
       if (2**j)&i:
           s.append(j)
    print(*s)
def search(k,s):
    if k==n:
        global c
        c+=1    
        return 0
    search(k+1,s)
    s.append(k)
    search(k+1,s)
    s.pop()
c=0
n=100
search(0,[])
print(c)
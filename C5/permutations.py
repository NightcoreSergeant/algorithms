def search(c,s):
    if len(s)==n:
        print(*s)
        return 0
    else:
        for i in range(n):
            if c[i]:
                continue
            c[i]=True
            s.append(i)
            search(c,s)
            s.pop()
            c[i]=False
n=5
chosen=[False]*n
search(chosen,[])
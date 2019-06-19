def search(y,column,diag1,diag2):
    if y==n:
        global c
        c+=1
    else:
        for i in range(n):
            if column[i] or diag1[i+y] or diag2[i-y+n-1]:
                continue
            column[i]=diag1[i+y]=diag2[i-y+n-1]=1
            search(y+1,column,diag1,diag2)
            column[i]=diag1[i+y]=diag2[i-y+n-1]=0
n=14
column=[0]*n
diag1=[0]*(n+n-1)
diag2=[0]*(n+n-1)
c=0
search(0,column,diag1,diag2)
print(c)
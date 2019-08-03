##O(n**3)
import time
start=time.time()
g=[]
n=int(input())
for i in range(n):
    s=list(map(int,list(input())))
    g.append(s)
ans=0
for i in range(n-1):
    for j in range(i+1,n):
        c=0
        for k in range(n):
            if g[i][k]&g[j][k]:
                c+=1
        ans+=c*(c-1)//2
end=time.time()
print(ans) 
print(end-start)


##O(n**4)
#g=[]
#n=int(input())
#for i in range(n):
#    s=list(map(int,list(input())))
#    g.append(s)
#ans=0
#for i in range(n-1):
#    for j in range(n):
#        for k in range(j+1,n):
#            if g[i][j]&g[i][k]:
#                for ni in range(i+1,n):
#                    if g[ni][j]&g[ni][k]:
#                        ans+=1
#print(ans)
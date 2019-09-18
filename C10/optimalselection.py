#def total(S,d):
#    if d==-1:
#        return 0
#    m=10**9
#    for i in range(n):
#        if i not in S:
#            S.add(i)
#            m=min((total(S,d-1)+price[d][i]),m)
#            S.remove(i)
#    return m
        
                 
price=[
[6,9,5,2,8,9,1,6],
[8,2,6,2,7,5,7,2],
[5,3,9,7,3,5,0,4]
]
n=len(price[0])
k=len(price)
#print(total(set(),k-1))

Z=1<<k
total=[[20]*n for i in range(Z)]

for x in range(k):
    total[1<<x][0]=price[x][0]

for d in range(1,n):
    for s in range(Z):
        total[s][d]=total[s][d-1]
        for x in range(k):
            if s&(1<<x):
               # print(x)
                total[s][d]=min(total[s][d],
                    total[s^(1<<x)][d-1]+price[x][d])
for i in total:
    print(*i)
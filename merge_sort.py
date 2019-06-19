#import random
def merge(alist):
    if len(alist)>1:
        mid = len(alist)//2
        l = alist[:mid]
        r = alist[mid:]
        merge(l)
        merge(r)
        i=j=k=0
        while i < len(l) and j < len(r):
            if l[i]<r[j]:
                alist[k]=l[i]
                i=i+1
            else:
                alist[k]=r[j]
                j=j+1
            print('change1',l)
            k=k+1
        while i<len(l):
            alist[k]=l[i]
            i=i+1
            k=k+1
            print('change2',l)
        while j<len(r):
            alist[k]=r[j]
            j=j+1
            k=k+1
            print('change3',l)
    return l

#l=[random.randrange(0,10) for i in range(10**1)]
#x=[i for i in l]
#merge(x)
#print(x)
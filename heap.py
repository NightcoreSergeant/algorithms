class Heap:
    INF=float('inf')
    #def __init__(self): 
    heap = []  
    
    def swap(self,a,b):
        a,b=b,a

    def parent(self,i):
        return (i)//2
    
    def childleft(self,i):
        return (i)*2+1
    
    def childright(self,i):
        return (i+1)*2
    
    def heappush(self,k):
        self.heap.append(k)
        i=len(self.heap)-1
        while i!=0 and self.heap[self.parent(i)]>self.heap[i]:
            self.heap[self.parent(i)],self.heap[i]=self.heap[i],self.heap[self.parent(i)]
            i=self.parent(i)
    
    def heappop(self,k):
        size=len(self.heap)-1
        self.heap[k]=-self.INF
        
        while k!=0 and self.heap[self.parent(k)]>self.heap[k]:
            self.heap[self.parent(k)],self.heap[k]=self.heap[k],self.heap[self.parent(k)]
            k=self.parent(k)
        self.heap[0]=self.heap.pop()
        
        #l=self.childleft(k)
        #r=self.childright(k)
        while k<size and self.childright(k)<size and self.childleft(k)<size and (self.heap[k]>self.heap[self.childleft(k)] or self.heap[k]>self.heap[self.childright(k)]):
            
            if self.heap[k]>self.heap[self.childleft(k)]:
                self.heap[k],self.heap[self.childleft(k)]=self.heap[self.childleft(k)],self.heap[k]
                k=self.childleft(k)
            else:
                self.heap[k],self.heap[self.childright(k)]=self.heap[self.childright(k)],self.heap[k]
                k=self.childright(k) 
        l=self.childleft(k)
        r=self.childright(k)
        
        if l<size and self.heap[k]>self.heap[l]:
            self.heap[k],self.heap[l]=self.heap[l],self.heap[k]
        elif r<size:
            self.heap[k],self.heap[r]=self.heap[r],self.heap[k]


    def smallest(self):
        return self.heap[0]

arr=Heap()
arr.heappush(10)
arr.heappush(5)
arr.heappush(4)
arr.heappush(3)
arr.heappop(0)
print(arr.smallest())
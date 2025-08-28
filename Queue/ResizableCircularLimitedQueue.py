class ResizableCircularLimitedQueue:
    
    default_size=5
    
    def __init__(self):
        self.Queue=[None]*ResizableCircularLimitedQueue.default_size
        self.count=0
        self.front=0
        
        
    def isEmpty(self):
        return self.count==0  
    
    def count(self):
        return self.count
    
    def getFirst(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.Queue[self.front]
    
    def enqueue(self,ele):
        if self.count==len(self.Queue):
            self.resize(len(self.Queue)*2)
        
        idx=(self.count+self.front)%len(self.Queue)
        self.Queue[idx]=ele
        self.count+=1
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        
        ele=self.Queue[self.front]
        self.Queue[self.front]=None
        self.count-=1
        self.front=(self.front+1)%len(self.Queue)
        
        if 0<self.count<=len(self.Queue)//4:
            self.resize(len(self.Queue)//2)
        return ele
    
    def resize(self,cap):
        old_data=self.Queue.copy()
        walk=self.front
        self.Queue=[None]*cap
        
        for k in range(self.count):
            self.Queue[k]=old_data[walk]
            walk=(walk+1)%len(old_data)
        self.front=0
    
    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.Queue   

Q=ResizableCircularLimitedQueue()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
Q.enqueue(60)
Q.enqueue(70)
#print(Q.display())

Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()



print(Q.display())




            
            
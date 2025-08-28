class LimitedQueue:
      
    default_size=5
    
    def __init__(self):
        self.Queue=[None]*LimitedQueue.default_size
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
            return "Queue is full"
        
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
        return ele
    
    
    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.Queue  
    
        

Q=LimitedQueue()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
#print(Q.display())

Q.dequeue()
Q.dequeue()
Q.dequeue()

Q.enqueue(60)


print(Q.display())

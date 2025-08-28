class LimitedQueueFIndMax:
      
    default_size=5
    
    def __init__(self):
        self.Queue=[None]*LimitedQueueFIndMax.default_size
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
    
    def find_max(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            max_val=self.Queue[0]
            for i in range(1,len(self.Queue)):
                if self.Queue[i] is not None and self.Queue[i]>max_val:
                    max_val=self.Queue[i]
            return max_val 
        

Q=LimitedQueueFIndMax()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)
Q.enqueue(40)
Q.enqueue(50)
#print(Q.display())

#Q.dequeue()
#.dequeue()
#Q.dequeue()

#Q.enqueue(60)
print("Max value in the queue:",Q.find_max())


print(Q.display())

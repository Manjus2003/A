class SimpleQueue:
    
    def __init__(self):
        self.Queue = []
    
    def isEmpty(self):
        return len(self.Queue)==0    
    
    def enqueue(self, item):
        self.Queue.append(item)
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            item = self.Queue[0]
            del self.Queue[0]
            return item
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.Queue[0]

    def display(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.Queue

queue=SimpleQueue()

queue.enqueue(10)
queue.enqueue(20)       
queue.enqueue(30)
print(queue.display())

queue.dequeue()
queue.dequeue()
print(queue.display())  
               
            
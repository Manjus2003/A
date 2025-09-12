class Stack:

    def __init__(self):
        self.top=0
        self.stack=[]
        
    def push(self,ele):
        self.top+=1
        self.stack.append(ele)

    def is_empty(self):
        return self.top==0    
    
    def pop(self):
        if self.is_empty():
            return 0
        else:
            self.stack.pop()
            self.top-=1

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top-1]

    def display(self):
        for i in self.stack[::-1]:
            print(i)



#s=Stack()



#s.pop()
#s.pop()



#s.display()

#s.peek()






        

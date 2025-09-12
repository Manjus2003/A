class LimitedStack:

    def __init__(self):
        self.top=0
        self.stack=[None]*5
        
    def push(self,ele):
        if not len(self.stack)==self.top:
            self.top+=1
            self.stack[self.top-1]=ele
        else:
            print("StackOverflow Error")


    def is_empty(self):
        return self.top==0    
    
    def pop(self):
        if self.is_empty():
            print("StackUderflow Error")
        else:
            self.stack.pop()
            self.top-=1

    def peek(self):
        if not self.is_empty():
            print(self.stack[self.top-1])
        else:
            print("No elements are present in the Stack")    

    def display(self):
        for i in self.stack[::-1]:
            print(i)



s=LimitedStack()




s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(60)
s.push(70)

s.pop()

s.display()

s.peek()